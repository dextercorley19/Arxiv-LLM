// pages/index.tsx

import { useState } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";

const Home: React.FC = () => {
  const [url, setUrl] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post("/api/process-url", { url });
      setMessage(response.data.message);
      setUrl(""); // Clear input field
    } catch (error) {
      setMessage("Error processing the URL");
      console.error(error);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-green-500 font-['JetBrains_Mono',_monospace] text-black">
      <Navbar />
      <div className="flex flex-col items-center justify-center">
        <form onSubmit={handleSubmit} className="flex items-center mb-4">
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Enter arXiv URL"
            id="url-input"
            className="p-2 text-black border border-gray-300 rounded-l-md"
            required
          />
          <button
            className="p-2 bg-black text-green-500 rounded-r-md"
            type="submit"
          >
            Submit
          </button>
        </form>
        {message && <p className="mt-4 text-black">{message}</p>}
      </div>
      <div className="flex flex-col justify-center items-center max-w-xl mx-auto">
        <p className="text-xl text-black text-center">
          Welcome to Arxiv LLM, please input the URL for a paper you'd like to
          learn more about (be patient after submitting)
        </p>
      </div>
    </div>
  );
};

export default Home;
