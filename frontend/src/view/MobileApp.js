import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route 
} from 'react-router-dom'
import NavBar from '../components/Navbar.js';
import MobileHomePage from "../components/MobileHome.js";
import CreateEvent from "../components/MobileCreateEvent.js";

const MobileApp = () => {
    return (
        <Router>
            {/* <NavBar/> */}
            <Routes>
                {/* <Route path='/create_event' Component={CreateEvent}/> */}
                <Route path='/' Component={MobileHomePage}/>
                <Route path='/CreateEvent' Component={CreateEvent}/>
            </Routes>
    </Router>
    )
}

export default MobileApp