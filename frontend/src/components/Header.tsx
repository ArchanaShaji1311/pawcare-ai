import { PawPrint } from "lucide-react";

export default function Header() {
  return (
    <header className="sticky top-0 z-30 backdrop-blur-md bg-white/70 border-b border-brand-100">
      <div className="max-w-6xl mx-auto px-5 h-16 flex items-center justify-between">
        <a href="#top" className="flex items-center gap-2 font-bold text-slate-800">
          <span className="grid place-items-center w-9 h-9 rounded-xl bg-brand-600 text-white shadow-lg shadow-brand-600/30">
            <PawPrint size={20} />
          </span>
          <span className="text-lg tracking-tight">
            Paw<span className="text-brand-600">Care</span>
            <span className="ml-1 text-[10px] font-semibold align-super text-accent-500">
              AI
            </span>
          </span>
        </a>
        <nav className="hidden sm:flex items-center gap-7 text-sm font-medium text-slate-600">
          <a href="#how" className="hover:text-brand-700 transition">
            How it works
          </a>
          <a href="#analyze" className="hover:text-brand-700 transition">
            Analyze
          </a>
          <a
            href="#analyze"
            className="px-4 py-2 rounded-full bg-brand-600 text-white shadow-md shadow-brand-600/25 hover:bg-brand-700 transition"
          >
            Try it free
          </a>
        </nav>
      </div>
    </header>
  );
}
