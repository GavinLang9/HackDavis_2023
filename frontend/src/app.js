import React from "react"
import { useState, useEffect } from "react"


export default function App() {

    const [message, setMessage] = useState('hello')

    useEffect(
        ()=>{
            fetch('user/users')
            .then(response=>response.json())
            .then(data=>{
                setMessage(data[0].name)
            })
            .catch(error=>console.log(error))

            
        },[]
    )

    return (
        <div className="app">
            {message}
        </div>
    )
}