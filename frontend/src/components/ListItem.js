import React from "react";
import { useState, useEffect } from "react";

const ListItem = (props) => {
    
    console.log(props)
    return (
        <div className="list-item">
            <div className="title">
                {/* org logo */}
                <h1>{props.props.name}</h1>
            </div>
            <p className="description">{props.props.description}</p>
            <div>
                <div className="location">
                    <h1>Location</h1>
                    <a href="">{props.props.address}</a>
                </div>
                <div className="date">
                    {props.props.start_time}
                </div>
            </div>
        </div>
    )
}

export default ListItem