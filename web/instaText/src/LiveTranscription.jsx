import React, { useState, useEffect } from 'react';

function LiveTranscription() {
    const [transcript, setTranscript] = useState('');
    const [isListening, setIsListening] = useState(false);

    useEffect(() => {
        let intervalId;

        if (isListening) {
            intervalId = setInterval(async () => {
                try {
                    const response = await fetch('http://localhost:5000/transcription');
                    const data = await response.json();
                    if (data.transcription) {
                        setTranscript((prev) => prev + ' ' + data.transcription);
                        console.log('Transcription fetched:', data.transcription);
                    }
                } catch (error) {
                    console.error('Error fetching transcription:', error);
                }
            }, 1000); // Poll every second
        }

        return () => clearInterval(intervalId); // Cleanup on unmount or when listening stops
    }, [isListening]);

    const handleStartListening = () => setIsListening(true);
    const handleStopListening = () => setIsListening(false);
    
    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold mb-4">Live Transcription</h1>
            <div className="border border-black p-2 h-52 overflow-y-scroll rounded bg-gray-100">
                {transcript || <p className="text-gray-400">Transcription will appear here...</p>}
            </div>
            <button
                onClick={isListening ? handleStopListening : handleStartListening}
                className={`mt-4 px-4 py-2 rounded text-white ${
                    isListening ? 'bg-red-500 hover:bg-red-700' : 'bg-blue-500 hover:bg-blue-700'
                }`}
            >
                {isListening ? 'Stop Listening' : 'Start Listening'}
            </button>
        </div>
    );
}

export default LiveTranscription;
