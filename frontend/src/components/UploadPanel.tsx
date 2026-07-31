import { useRef, useState } from "react";
import { UploadCloud, X, Stethoscope, Loader2 } from "lucide-react";
import { BREED_OPTIONS } from "../api";

interface Props {
  onAnalyze: (data: { image: File; symptoms: string; breed: string }) => void;
  loading: boolean;
}

export default function UploadPanel({ onAnalyze, loading }: Props) {
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [symptoms, setSymptoms] = useState("");
  const [breed, setBreed] = useState("");
  const [dragging, setDragging] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  function selectFile(f: File | undefined) {
    if (!f) return;
    if (!f.type.startsWith("image/")) {
      setError("Please choose an image file.");
      return;
    }
    setError(null);
    setFile(f);
    setPreview(URL.createObjectURL(f));
  }

  function clearFile() {
    setFile(null);
    if (preview) URL.revokeObjectURL(preview);
    setPreview(null);
    if (inputRef.current) inputRef.current.value = "";
  }

  function submit() {
    if (!file) {
      setError("Upload a photo of your dog to continue.");
      return;
    }
    const chosenBreed = breed === "Other / Mixed" ? "" : breed;
    onAnalyze({ image: file, symptoms: symptoms.trim(), breed: chosenBreed });
  }

  return (
    <div className="rounded-3xl bg-white border border-slate-100 shadow-xl shadow-slate-900/5 p-6 sm:p-8">
      <h3 className="text-xl font-bold text-slate-900 flex items-center gap-2">
        <Stethoscope className="text-brand-600" size={22} /> Health check
      </h3>
      <p className="text-slate-500 text-sm mt-1">
        Add a clear photo and any symptoms you've noticed.
      </p>

      <div
        onDragOver={(e) => {
          e.preventDefault();
          setDragging(true);
        }}
        onDragLeave={() => setDragging(false)}
        onDrop={(e) => {
          e.preventDefault();
          setDragging(false);
          selectFile(e.dataTransfer.files?.[0]);
        }}
        onClick={() => !preview && inputRef.current?.click()}
        className={`mt-5 relative rounded-2xl border-2 border-dashed transition cursor-pointer ${
          dragging
            ? "border-brand-500 bg-brand-50"
            : "border-slate-200 hover:border-brand-300 bg-slate-50/60"
        }`}
      >
        {preview ? (
          <div className="relative">
            <img
              src={preview}
              alt="Selected dog"
              className="w-full h-64 object-cover rounded-2xl"
            />
            <button
              onClick={(e) => {
                e.stopPropagation();
                clearFile();
              }}
              className="absolute top-3 right-3 grid place-items-center w-8 h-8 rounded-full bg-black/60 text-white hover:bg-black/80"
              aria-label="Remove image"
            >
              <X size={16} />
            </button>
          </div>
        ) : (
          <div className="py-12 flex flex-col items-center text-center px-4">
            <span className="grid place-items-center w-14 h-14 rounded-2xl bg-brand-100 text-brand-600 mb-3">
              <UploadCloud size={26} />
            </span>
            <p className="font-semibold text-slate-700">
              Drop a photo here or click to browse
            </p>
            <p className="text-xs text-slate-400 mt-1">JPG or PNG, up to 10MB</p>
          </div>
        )}
        <input
          ref={inputRef}
          type="file"
          accept="image/*"
          className="hidden"
          onChange={(e) => selectFile(e.target.files?.[0])}
        />
      </div>

      <div className="mt-5 grid gap-4">
        <div>
          <label className="text-sm font-semibold text-slate-700">Breed</label>
          <select
            value={breed}
            onChange={(e) => setBreed(e.target.value)}
            className="mt-1.5 w-full rounded-xl border border-slate-200 bg-white px-3 py-2.5 text-sm text-slate-700 focus:border-brand-400 focus:ring-2 focus:ring-brand-100 outline-none"
          >
            <option value="">Select a breed (optional)</option>
            {BREED_OPTIONS.map((b) => (
              <option key={b} value={b}>
                {b}
              </option>
            ))}
          </select>
        </div>

        <div>
          <label className="text-sm font-semibold text-slate-700">
            Symptoms &amp; observations
          </label>
          <textarea
            value={symptoms}
            onChange={(e) => setSymptoms(e.target.value)}
            rows={3}
            placeholder="e.g. Red itchy patch on belly, scratching a lot, small scab near the ear…"
            className="mt-1.5 w-full rounded-xl border border-slate-200 bg-white px-3 py-2.5 text-sm text-slate-700 resize-none focus:border-brand-400 focus:ring-2 focus:ring-brand-100 outline-none"
          />
        </div>
      </div>

      {error && (
        <p className="mt-3 text-sm text-red-600 bg-red-50 rounded-lg px-3 py-2">
          {error}
        </p>
      )}

      <button
        onClick={submit}
        disabled={loading}
        className="mt-5 w-full py-3.5 rounded-xl bg-brand-600 text-white font-semibold shadow-lg shadow-brand-600/25 hover:bg-brand-700 disabled:opacity-60 disabled:cursor-not-allowed transition flex items-center justify-center gap-2"
      >
        {loading ? (
          <>
            <Loader2 size={18} className="animate-spin" /> Analyzing…
          </>
        ) : (
          "Analyze health"
        )}
      </button>
    </div>
  );
}
