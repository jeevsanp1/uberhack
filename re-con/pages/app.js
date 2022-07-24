import Head from 'next/head'
import Image from 'next/image'
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