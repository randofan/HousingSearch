import React, {useState} from 'react';
import {MapContainer} from 'react-leaflet'


const App = () => {
  const [houses, setHouses] = useState<Record<string, any>[]>([])
  const [filters, setFilters] = useState<Record<string, any>>({
    beds: null,
    baths: null,
    price: null,
    area: null,
    pets: null,
    parking: null,
    laundry: null,
    apartment: null,
    townhouse: null,
    house: null
  })

  return (
    <div>
        <form onSubmit={async () => {
          try {
            const res = await fetch(`/search?${Object.keys(filters).filter(key => String(filters[key]))
                                                                   .map(key => key + '=' + String(filters[key])).join('&')}`)
            if (!res.ok) {
              alert("Incorrect Input")
              return
            }
            const parse = await res.json()
            setHouses(JSON.parse(parse))
          } catch(e) {
            alert("Error contacting server")
            console.log(e)
          }
        }}>
          {Object.keys(filters).map(key => {
            return (
              <label>
              {key}
              {typeof(filters[key]) == 'number' ? 
                <input key={key} type='number' onChange={(e) => setFilters({...filters, key: e.target.value})} /> : 
                <input key={key} type='checkbox' onChange={(e) => setFilters({...filters, key: e.target.checked})} />}
              </label> 
            )
          })}
          <input type='submit' value='Submit'/>
        </form>
        <MapContainer />
        <ul>
          {houses.map((house, i) => <li key={i+1}>{house['address']}</li>)}
        </ul>
    </div>
  );
}

export default App;
