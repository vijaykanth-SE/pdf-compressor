import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
  const [filecount, setCount] = useState(0)

  return (
    <div>
      <h1>PDF Compressor</h1>
      <p>Files selected: {filecount}</p>
      <button onClick={()=>setCount(filecount+1)}>Add file</button>
      <button onClick={()=>setCount(0)}>Reset</button>
    </div>
  )
}

export default App
