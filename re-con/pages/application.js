import Head from 'next/head'
import styles from '../styles/Home.module.css'

export default function App() {
   
    return (
        <div className={styles.container}>
          <Head>
            <title>Renewable Energy Consultant</title>
            <meta name="description" content="Find Your Future" />
            <link rel="icon" href="/favicon.ico" />
          </Head>
    
          <main className={styles.main}>
            <h1 className={styles.apptitle}>
                Renewable Energy Consultant
            </h1> 
              
            <form action="/send-data-here" method="post">
            <ul>
              <li><label for="first">Longitude: </label>
              <input type="text" id="first" name="first" /></li>
              <li><label for="first">Latitude: </label>
              <input type="text" id="first" name="first" /></li>
              <li><label for="first">State: </label>
              <input type="text" id="first" name="first" /></li>
              <li><button type="submit">Submit</button></li>
            </ul>
            </form>

          </main>
    
          {/* I don't think we need this */}
          {/* <footer className={styles.footer}>
            <a
              href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
              target="_blank"
              rel="noopener noreferrer"
            >
              Powered by{' '}
              <span className={styles.logo}>
                <Image src="/ReCon.png" alt="ReCon"/>
              </span>
            </a>
          </footer> */}
        </div>
      )
}