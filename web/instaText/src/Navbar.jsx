import logo from './assets/logo.svg';

function Navbar() {
    return (
        <div className="flex justify-around items-center w-full h-20 bg-[#D9D9D9]">   
            <div className="flex gap-2">
                {<img src={logo} alt="logo" className="w-10 h-10"/>}
                <h1 className="text-3xl font-bold">InstaText</h1>
            </div>
            <div className="flex gap-10 items-center">
                <ul className="flex gap-10 text-xl">
                    <li>
                        <a href="#" className="group text-black transition-all duration-300 ease-in-out">
                            <span className="bg-left-bottom bg-gradient-to-r from-black to-black bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out">
                                Home
                            </span>
                        </a>
                    </li>
                    <li>
                        <a href="#" className="group text-black transition-all duration-300 ease-in-out">
                            <span className="bg-left-bottom bg-gradient-to-r from-black to-black bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out">
                                About
                            </span>
                        </a>
                    </li>
                </ul>
                <button className="border-primary border bg-white text-[#FFBD03] font-semibold rounded-full text-lg px-4 py-2 border-1 border-[#FFBD03] transition-all duration-300 ease-in-out hover:bg-[#FFBD03] hover:text-black">
                    Try Out
                </button>
            </div>
        </div>
    );
}

export default Navbar;