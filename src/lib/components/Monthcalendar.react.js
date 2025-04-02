import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import './Monthcalendartheme.css';


const Monthcalendar = (props) => {
    const { id, selectedDate, className, setProps } = props;

    const [startDate, setStartDate] = useState(selectedDate ? new Date(selectedDate) : new Date());

    // Sync startDate with selectedDate prop when it changes
    useEffect(() => {
        if (selectedDate) {
            setStartDate(new Date(selectedDate));
        }
    }, [selectedDate]);

    return (
        <div id={id} className={className}>
            <DatePicker
                selected={startDate}
                onChange={(date) => {
                    setStartDate(date);
                    setProps({ selectedDate: date.toISOString() });
                }}
                dateFormat="yyyy/MM"
                showMonthYearPicker
            />
        </div>
    );
};

Monthcalendar.defaultProps = {
    selectedDate: null,
};

Monthcalendar.propTypes = {
    id: PropTypes.string,
    selectedDate: PropTypes.string,
    className: PropTypes.string,
    setProps: PropTypes.func,
};

export default Monthcalendar;
