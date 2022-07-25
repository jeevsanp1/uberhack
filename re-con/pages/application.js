import axios from 'axios'
import Head from 'next/head'
import Image from 'next/image'
import { useState } from 'react'
import styles from '../styles/Home.module.css'

import Output from './output'

export default function App() {
    const [lng, setLng] = useState('')
    const [lat, setLat] = useState('')
    const [state, setState] = useState('')
    const [budget, setBudget] = useState(null)
    const [autoed, setAutoed] = useState(false);
    const [river, setRiver] = useState(false);

    const [loading, setLoading] = useState(false);

    const [hydro, setHydro] = useState(null);
    const [solar, setSolar] = useState(null);
    const [wind, setWind] = useState(null);

    const autoFill = () => {
      navigator.geolocation.getCurrentPosition((pos) => {
        fetch(`https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${pos.coords.latitude}&longitude=${pos.coords.longitude}&localityLanguage=en`)
          .then((res) => {
            return res.json()
          })
          .then((j) => {
            setAutoed(true);
            setLat(j.latitude)
            setLng(j.longitude)
            setState(j.principalSubdivision)
          })
      }, (e) => {
        console.log(e);
      }) 
    }

    const fetcher = () => {
      const url = (`https://uber-hack-flask-api.herokuapp.com/${lat}/${lng}/${river}/${budget}/${state}`)
      setLoading(true)
      axios.get(url)
        .then(res => {
          if(res.status == 200) {
            setHydro(res.data.hydro)
            setSolar(res.data.solar)
            setWind(res.data.wind)
            setLoading(false);
          } else {
            alert('Error Fetching')
          }
        })
    }

    const submit = () => {
      if(setAutoed && budget != null) {
        fetcher()
      } else if(lng != '' && lat != '' && state != '' && budget != null) {
        fetcher()
      } else {
        alert('Error: Fields are Missing')
      }
    }
   
    return (
        <div className={styles.container}>
          <Head>
            <title>Renewable Energy Consultant</title>
            <meta name="description" content="Find Your Future" />
            <link rel="icon" href="/favicon.ico" />
          </Head>

          <main className={styles.main}>
            <h1 className={styles.renew}>
                Renewable Energy Consultant
            </h1> 
              
            <input placeholder="Latitude: " className={styles.Lat} value={lat} onChange={(e) => {
              setLat(e.target.value)
            }} />
            <input placeholder="Longitude: " className={styles.Lat} value={lng} onChange={(e) => {
              setLng(e.target.value)
            }} />
            <input placeholder='State: ' className={styles.Lat} value={state} onChange={(e) => {
              setState(e.target.value)
            }} />
            <input placeholder="Budget: " className={styles.Lat} value={budget} onChange={(e) => {
              const x = parseInt(e.target.value);
              if(isNaN(parseInt(e.target.value))) {
                alert('Invalid Input, must be a number')
                setBudget(0)
              } else {
                setBudget(x);
              }
            }} />

            <p className={styles.river}>River Near You: </p> <input type="checkbox" className={styles.checkbox} checked={river} onChange={(_) => {
              setRiver(!river)
            }} />

            <button onClick={autoFill} className={styles.Button}>Auto-Fill Location Data</button>
            <button onClick={submit} className={styles.Button}>Submit</button>

          <h1 className={styles.lonfind}><a href='https://www.latlong.net/'>What is my latitude and longitude?</a></h1>
          {
            loading ? <p>Loading ...</p> : null
          }
          {
            
            hydro ? <Output hydro={hydro} solar={solar} wind={wind} /> : null
          }
          </main>
    
          <footer className={styles.footer}>
            <a
              href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
              target="_blank"
              rel="noopener noreferrer"
            >
              Powered by{' '}
              <span className={styles.logo}>
                <Image src="/ReCon.png" alt="ReCon" width={72} height={16} />
              </span>
            </a>
          </footer>
        </div>
      )
}