
import './HeroSection.css';

function HeroSection() {
    return (
        <div className="flex bg-[#83A3FF] w-full h-[480px] opacity-20 justify-center">
            <div className="flex flex-col w-3/4 items-end justify-center gap-6">
                <h1 id="headline"className="text-white text-6xl w-1/2 [text-shadow:_0_1px_0_rgb(0_0_0_/_40%)]">Welcome to the InstaText!</h1>
                <p id="description" className="text-white text-xl w-1/2">Overcome language barriers and hearing challenges with our seamless transcription technology</p>
            </div>
        </div>
    )
}

export default HeroSection;