import React, { Component } from "react";
import axios from "axios";

export default class Header extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "",
        };
    }

    componentDidMount() {
        this.usernameOfCurrentUser();
    }

    usernameOfCurrentUser() {
        axios
            .get("/api/users/current")
            .then((res) => this.setState({ username: res.data.username }))
            .catch((err) => console.log(err));
    }

    render() {
        return (
            <div class="header">
                <nav class="navbar navbar-light bg-light m-3">
                    <a class="navbar-brand" href="/">
                        <img class="d-inline-block align-top p-1" width="30" height="30" src={process.env.PUBLIC_URL + '/logo-512x512.png'} alt={"logo"} /> 
                        <span class="d-none d-md-inline font-weight-bold">Todo App</span>
                    </a>
                    <span class="navbar-text text-lowercase text-dark font-weight-bold">
                        { this.state.username }
                    </span>
                </nav>
                <h1 className="text-white text-uppercase text-center font-weight-bold my-4">Todo app</h1>
            </div>
        );
    }
}
