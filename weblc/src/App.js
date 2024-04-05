import './App.css'
import React, { useEffect } from 'react';
import { useState } from 'react';
import createModule from "./add.mjs";

function App() {
  const [retrn, setRetrn] = useState();
  const [name,setName] = useState("");
  const [result,setResult] = useState("");
  const [registers, setRegisters] = useState([
    { R_R0: 0, R_R1: 0, R_R2: 0, R_R3: 0, R_R4: 0, R_R5: 0, R_R6: 0, R_R7: 0, R_PC: 0, R_COND: 0, R_COUNT: 0 }
  ]);

  const handleNext = () => {
    setRegisters([...registers,    { R_R0: 1, R_R1: 2, R_R2: 3, R_R3: 0, R_R4: 0, R_R5: 0, R_R6: 0, R_R7: 0, R_PC: 0, R_COND: 0, R_COUNT: 0 }
    ])
  };

  const handleExecuteAll = () => {
    console.log("all");
  };

  useEffect(() => { 
    createModule().then((Module) => {    
      setRetrn(() => Module.cwrap("locker", "string", ["string"]));    
    });  }, []);  
      if (!retrn) {    
        return "Loading webassembly...";  
      }

  const handleClick= ()=>{
    setResult(retrn(name))
  }
  const headings = Object.keys(registers[0]);
  return (
    <div className="App">
     <input onChange={e=>{setName(e.target.value)}}></input>
     <button onClick={()=>handleClick()}>Lock/Unlock</button>
     <p>Status:{result}</p>
     <div>
      <div>
        <button onClick={handleNext}>Next</button>
        <button onClick={handleExecuteAll}>Execute All</button>
      </div>
      <table>
        <thead>
          <tr>
            {headings.map((heading, index) => (
              <th key={index}>{heading}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {registers.map((register, index) => (
            <tr key={index}>
              {headings.map((heading, index) => (
                <td key={index}>{register[heading]}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
    </div>
  );
}

export default App;