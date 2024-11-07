import Navbar from './Navbar.jsx';
import HeroSection from './HeroSection.jsx';
import AboutSection from './AboutSection.jsx';
import LiveTranscription from './LiveTranscription.jsx';
import { react, useState } from 'react';

function App() {
  const [count, setCount] = useState(0)



  return (
    <div>
      <Navbar/>
      <HeroSection/>
      <AboutSection/>
      <hr></hr>
      <LiveTranscription/>
    </div>
  )
}

export default App;
