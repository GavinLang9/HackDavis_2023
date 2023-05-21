import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route 
} from 'react-router-dom'
import NavBar from "../components/Navbar";
import DesktopHomePage from "../components/DesktopHome";

const DesktopApp = () => {
    return (
      <Router>
        <NavBar/>
          <Routes>
            {/* <Route path='/create_event' Component={CreateEvent}/> */}
            <Route path='/' Component={DesktopHomePage}/>
          </Routes>
      </Router>
    )
}

export default DesktopApp