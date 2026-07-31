function Bar({ className = "" }: { className?: string }) {
  return <div className={`skeleton ${className}`} />;
}

export default function PageSkeleton() {
  return (
    <div className="min-h-screen">
      <div className="h-16 border-b border-slate-100 dark:border-slate-800">
        <div className="max-w-6xl mx-auto px-5 h-full flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Bar className="w-9 h-9 rounded-xl" />
            <Bar className="w-24 h-5" />
          </div>
          <div className="flex items-center gap-4">
            <Bar className="hidden sm:block w-20 h-5" />
            <Bar className="w-24 h-9 rounded-full" />
            <Bar className="w-9 h-9 rounded-full" />
          </div>
        </div>
      </div>

      <div className="max-w-6xl mx-auto px-5 py-12 grid md:grid-cols-2 gap-12 lg:gap-16 items-center min-h-[calc(100vh-4rem)]">
        <div className="space-y-5">
          <Bar className="w-56 h-7 rounded-full" />
          <div className="space-y-3">
            <Bar className="w-11/12 h-12" />
            <Bar className="w-8/12 h-12" />
          </div>
          <div className="space-y-2 pt-2">
            <Bar className="w-full h-4" />
            <Bar className="w-10/12 h-4" />
            <Bar className="w-9/12 h-4" />
          </div>
          <div className="flex gap-2 pt-2">
            <Bar className="w-24 h-8 rounded-full" />
            <Bar className="w-28 h-8 rounded-full" />
            <Bar className="w-20 h-8 rounded-full" />
            <Bar className="w-24 h-8 rounded-full" />
          </div>
          <div className="flex gap-4 pt-2">
            <Bar className="w-40 h-12 rounded-full" />
            <Bar className="w-40 h-12 rounded-full" />
          </div>
          <div className="flex gap-8 pt-6">
            <Bar className="w-20 h-10" />
            <Bar className="w-20 h-10" />
            <Bar className="w-20 h-10" />
          </div>
        </div>

        <div className="mx-auto w-full max-w-md">
          <div className="rounded-[2.5rem] border border-slate-100 dark:border-slate-700 p-6 sm:p-7 space-y-5">
            <Bar className="w-full h-60 rounded-2xl" />
            <Bar className="w-24 h-3" />
            <div className="space-y-4">
              <Bar className="w-full h-6" />
              <Bar className="w-full h-6" />
              <Bar className="w-full h-10 rounded-xl" />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
