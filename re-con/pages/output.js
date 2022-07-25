import { useState } from "react";

const Output = (props) => {
    const [cur, _] = useState({
        'hydro': parseInt(props.hydro),
        'wind': parseInt(props.wind),
        'solar': parseInt(props.solar)
    })

    return (
        <div>
            Hydro: {cur.hydro}
            Wind: {cur.wind}
            Solar: {cur.solar}
        </div>
    )
}

export default Output;