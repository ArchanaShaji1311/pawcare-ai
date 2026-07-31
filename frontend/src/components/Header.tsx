import { PawPrint, Moon, Sun } from "lucide-react";

interface Props {
  isDark: boolean;
  onToggleTheme: () => void;
}

export default function Header({ isDark, onToggleTheme }: Props) {
  return (
    <header className="sticky top-0 z-30 backdrop-blur-md bg-white/70 dark:bg-slate-900/70 border-b border-brand-100 dark:border-slate-800">
      <div className="max-w-6xl mx-auto px-5 h-16 flex items-center justify-between">
        <a
          href="#top"
          className="flex items-center gap-2 font-bold text-slate-800 dark:text-slate-100"
        >
          <span className="grid place-items-center w-9 h-9 rounded-xl bg-brand-600 text-white shadow-lg shadow-brand-600/30">
            <PawPrint size={20} />
          </span>
          <span className="text-lg tracking-tight">
            Paw<span className="text-brand-600 dark:text-brand-400">Care</span>
            <span className="ml-1 text-[10px] font-semibold align-super text-accent-500">
              AI
            </span>
          </span>
        </a>
        <nav className="flex items-center gap-4 sm:gap-6 text-sm font-medium text-slate-600 dark:text-slate-300">
          <a
            href="#how"
            className="hidden sm:inline hover:text-brand-700 dark:hover:text-brand-300 transition"
          >
            How it works
          </a>
          <a
            href="#analyze"
            className="px-4 py-2 rounded-full bg-brand-600 text-white shadow-md shadow-brand-600/25 hover:bg-brand-700 transition"
          >
            Try it free
          </a>
          <button
            onClick={onToggleTheme}
            aria-label={isDark ? "Switch to light mode" : "Switch to dark mode"}
            className="grid place-items-center w-9 h-9 rounded-full border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:border-brand-300 dark:hover:border-brand-500 hover:text-brand-600 dark:hover:text-brand-400 transition"
          >
            {isDark ? <Sun size={18} /> : <Moon size={18} />}
          </button>
        </nav>
      </div>
    </header>
  );
}
