// pages/ask.tsx

import { useState } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";

const Ask: React.FC = () => {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post("/api/ask-question", { question });
      setAnswer(response.data.answer);
      setQuestion(""); // Clear input field
    } catch (error) {
      setAnswer("Error getting answer");
      console.error(error);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-green-500 font-['JetBrains_Mono',_monospace] text-black">
      <Navbar />
      <div className="flex flex-col items-center">
        <form onSubmit={handleSubmit} className="flex items-center mb-4">
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Type your question"
            className="p-2 text-black border border-gray-300 rounded-l-md"
            required
          />
          <button
            type="submit"
            className="p-2 bg-black text-green-500 rounded-r-md"
          >
            Submit
          </button>
        </form>
        <div>
          <h2 className="text-xl pl-4 mb-2">Response:</h2>
          {answer && <p className="mt-4 pl-4 text-black">Answer: {answer}</p>}
        </div>
      </div>
    </div>
  );
};

export default Ask;
