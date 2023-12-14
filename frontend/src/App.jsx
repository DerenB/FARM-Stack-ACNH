import './styles/App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import { Bugs, Home, Notfound } from './pages';

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/home" element={<Home />} />
          <Route path="/bugs" element={<Bugs />} />
          <Route path="*" element={<Notfound />} />
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App;