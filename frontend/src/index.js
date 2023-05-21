import React from 'react';
import ReactDOM from 'react-dom/client';
// import App from './app';
import {
  BrowserRouter as Router,
  Routes,
  Route 
} from 'react-router-dom'
import { useMediaQuery } from 'react-responsive'

// import NavBar from './components/Navbar.js';
import DesktopApp from './view/DesktopApp.js';
import MobileApp from './view/MobileApp.js';



const App = () => {
  const isMobile = useMediaQuery({
    query: "(max-width: 600px)"
  })
  const isDesktop = useMediaQuery({
    query: "(min-width: 1200px)"
  })  

  return (
    <div>
    {isMobile && !isDesktop ? <MobileApp/> : <DesktopApp/>}
    </div>
  )
}




const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <App/>
);

