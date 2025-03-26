/* eslint no-magic-numbers: 0 */
import React, { useState } from 'react';

import { Monthcalendar } from '../lib';

const App = () => {

    const [state, setState] = useState({value:'', label:'Type Here'});
    const setProps = (newProps) => {
            setState(newProps);
        };

    return (
        <div>
            <Monthcalendar
                setProps={setProps}
                {...state}
            />
        </div>
    )
};


export default App;
