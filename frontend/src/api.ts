import axios from "axios";
import type { AnalyzeResponse } from "./types";

const API_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

export interface AnalyzeParams {
  image: File;
  symptoms?: string;
  breed?: string;
}

export async function analyzeDog({
  image,
  symptoms,
  breed,
}: AnalyzeParams): Promise<AnalyzeResponse> {
  const form = new FormData();
  form.append("image", image);
  if (symptoms) form.append("symptoms", symptoms);
  if (breed) form.append("breed", breed);

  try {
    const { data } = await axios.post<AnalyzeResponse>(
      `${API_URL}/api/analyze`,
      form,
    );
    return data;
  } catch (err) {
    if (axios.isAxiosError(err) && err.response?.data?.detail) {
      throw new Error(err.response.data.detail as string);
    }
    throw new Error("Something went wrong while analyzing the image.");
  }
}

export async function checkHealth(): Promise<{
  status: string;
  gemini_enabled: boolean;
}> {
  const { data } = await axios.get(`${API_URL}/api/health`);
  return data;
}

export const BREED_OPTIONS = [
  "Labrador Retriever",
  "German Shepherd",
  "Golden Retriever",
  "French Bulldog",
  "Bulldog",
  "Poodle",
  "Beagle",
  "Dachshund",
  "Rottweiler",
  "Yorkshire Terrier",
  "Other / Mixed",
];
