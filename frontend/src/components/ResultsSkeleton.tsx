function Shimmer({ className = "" }: { className?: string }) {
  return <div className={`skeleton ${className}`} />;
}

export default function ResultsSkeleton() {
  return (
    <div className="space-y-5" aria-busy="true" aria-label="Analyzing">
      <div className="rounded-3xl bg-white dark:bg-slate-800 border border-slate-100 dark:border-slate-700 shadow-xl shadow-slate-900/5 dark:shadow-black/30 p-6 sm:p-8">
        <div className="flex items-center justify-between gap-3">
          <div className="space-y-2">
            <Shimmer className="h-5 w-40" />
            <Shimmer className="h-3 w-24" />
          </div>
          <div className="space-y-2 text-right">
            <Shimmer className="h-3 w-20 ml-auto" />
            <Shimmer className="h-7 w-14 ml-auto" />
          </div>
        </div>
        <div className="mt-4 space-y-2">
          <Shimmer className="h-3 w-full" />
          <Shimmer className="h-3 w-11/12" />
          <Shimmer className="h-3 w-3/4" />
        </div>
      </div>

      <div className="rounded-2xl border border-slate-100 dark:border-slate-700 bg-white dark:bg-slate-800 p-4 flex items-center gap-3">
        <Shimmer className="h-6 w-6 rounded-full" />
        <Shimmer className="h-4 w-56" />
      </div>

      <div className="grid sm:grid-cols-2 gap-3">
        {[0, 1].map((i) => (
          <div
            key={i}
            className="rounded-2xl border border-slate-100 dark:border-slate-700 bg-white dark:bg-slate-800 p-4 space-y-3"
          >
            <div className="flex items-center justify-between">
              <Shimmer className="h-4 w-32" />
              <Shimmer className="h-5 w-16 rounded-full" />
            </div>
            <Shimmer className="h-3 w-full" />
            <Shimmer className="h-3 w-2/3" />
            <div className="flex items-center justify-between pt-1">
              <Shimmer className="h-3 w-20" />
              <Shimmer className="h-2 w-28 rounded-full" />
            </div>
          </div>
        ))}
      </div>

      <div className="rounded-3xl bg-white dark:bg-slate-800 border border-slate-100 dark:border-slate-700 p-6 space-y-4">
        <Shimmer className="h-4 w-44" />
        <div className="flex gap-2">
          <Shimmer className="h-8 w-20 rounded-full" />
          <Shimmer className="h-8 w-24 rounded-full" />
          <Shimmer className="h-8 w-20 rounded-full" />
        </div>
        {[0, 1, 2].map((i) => (
          <div key={i} className="flex gap-3">
            <Shimmer className="h-7 w-7 rounded-lg shrink-0" />
            <div className="flex-1 space-y-2">
              <Shimmer className="h-3 w-40" />
              <Shimmer className="h-3 w-full" />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
