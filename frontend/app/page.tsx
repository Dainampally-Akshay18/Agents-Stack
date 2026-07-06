"use client"
import Image from "next/image";
import { useState } from "react";

export default function Home() {

  const [question, setQuestion] = useState("");
  const[answer, setAnswer] = useState("");

  const askQuestion = async () => {
    const response= await fetch("http://localhost:8000/api/chatbot", {
      method:"POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question }),
    });

    const data = await response.json();
    console.log(data)
    setAnswer(data.response);
  }

  return (
    <>
    <div className="">
      <input type="text " placeholder ="Ask a question " value={question} className="" onChange={(e)=>setQuestion(e.target.value)}/>
      <br /><br />
      <button className="bg-black" onClick={askQuestion}>
        Ask
      </button>

      <br /><br /><br /><br /><br />

      <div style={{border:"1px solid black", width:"500px", height:"200px", marginTop:"30px"}}>
        <h3>Answer</h3>
        <p className="text-black">{answer}</p>

      </div>
            </div>
    </>
  );
}
