import React from "react";
import { useState, useEffect } from "react";
const DesktopHomePage = () => {
    const [searchText, setSearchText] = useState('')


    const [isMobile, setIsMobile] = useState(window.innerWidth <= 600)

    // const handleScreenChange = (e) => {
    //     setIsMobile(e.target.innerWidth)
    // }

    // window.addEventListener('resize', handleScreenChange)

    
    // const handleSearchChange = (e) => {
    //     setSearchText(e.target.value)
    //     fetch("/search", method={'GET'})
    //     .then(response=>response.json())
    //     .then(data=> {
    //         console.log(data)
    //     })
    //     console.log(e)
    // }

    return (
        <div className="home">
            <h1>Home Page Desktop</h1>
            <input type='text' id='searchBar' /*onChange={handleSearchChange}*/ value={searchText}/>

        </div>
    )
}

export default DesktopHomePage