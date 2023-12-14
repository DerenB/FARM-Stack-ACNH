import React from 'react';

import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className='container mx-auto h-12'>
      <div className='flex flex-row text-start h-full w-full'>
        <div className='flex flex-row h-full w-3/4'>
          <a href="/home" className='flex bg-red-600 w-48 justify-center items-center text-2xl border-b-2 border-l-2 border-black'>Home</a>
          <a href="/bugs" className='flex bg-green-500 w-48 justify-center items-center text-2xl border-b-2 border-l-2 border-black'>All Bugs</a>
          <a href="/fish" className='flex bg-red-600 w-48 justify-center items-center text-2xl border-b-2 border-l-2 border-black'>All Fish</a>
          <a href="/sea" className='flex bg-green-500 w-48 justify-center items-center text-2xl border-b-2 border-l-2 border-r-2 border-black '>All Sea</a>
        </div>
        <div className='flex h-full w-1/4 justify-end'>
          <div className='flex bg-purple-600 h-full w-48 justify-center items-center text-2xl border-b-2 border-l-2 border-r-2 border-black'>
            Theme
          </div>
        </div>
      </div>
    </nav>
  )
};

export default Navbar;