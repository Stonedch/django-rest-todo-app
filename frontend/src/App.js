import React, { Component } from "react";
import Modal from "./components/Modal";
import Header from "./components/Header";
import TaskList from "./components/TaskList";
import axios from "axios";

class App extends Component {
    render() {
        return (
            <main>
                <Header/>
            </main>
        );
    }
}

export default App;
