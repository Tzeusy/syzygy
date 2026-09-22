export type ReobserveStateResult<M> =
  | { readonly kind: 'reobserved'; readonly model: M }
  | { readonly kind: 'failed'; readonly reason: string };

export interface ReobserveStateOptions<C, M> {
  readonly capture: C;
  readonly model: M;
  readonly observe: () => Promise<C>;
  readonly build: (capture: C) => M;
}

/** Owns the daemon's mutable evaluation pointer. A successful observation
 * builds completely before either capture or model is swapped; concurrent
 * callers share one in-flight operation, and failure preserves both. */
export function createReobserveState<C, M>(options: ReobserveStateOptions<C, M>): {
  readonly get: () => M;
  readonly getCapture: () => C;
  readonly replace: (capture: C, model: M) => void;
  readonly reobserve: () => Promise<ReobserveStateResult<M>>;
} {
  let capture = options.capture;
  let model = options.model;
  let inFlight: Promise<ReobserveStateResult<M>> | undefined;
  return {
    get: () => model,
    getCapture: () => capture,
    replace: (nextCapture, nextModel) => {
      capture = nextCapture;
      model = nextModel;
    },
    reobserve: async () => {
      if (inFlight !== undefined) return inFlight;
      inFlight = (async () => {
        try {
          const nextCapture = await options.observe();
          const nextModel = options.build(nextCapture);
          capture = nextCapture;
          model = nextModel;
          return { kind: 'reobserved', model: nextModel } as const;
        } catch (error: unknown) {
          return { kind: 'failed', reason: error instanceof Error ? error.message : String(error) } as const;
        }
      })().finally(() => { inFlight = undefined; });
      return inFlight;
    },
  };
}
