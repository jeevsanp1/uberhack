import Head from 'next/head'
import styles from '../styles/Home.module.css'
// import 'animate.css';

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Renewable Energy Consultant</title>
        <meta name="description" content="Find Your Future" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <div className={styles.welcome}>
        <h1 className={styles.title}>
        FIND YOUR <br /> RENEWABLE ENERGY FUTURE
        </h1>
        </div>
        <div>
          <h1 className={styles.about}>About Re-Con</h1>
          <h3 className={styles.about_content}>Climate change is one of the biggest problems in recent history. With our software Renewable Energy Consultant (ReCon), corporations and individuals can input simple data and can find what energy source and provider is best for their location and budget. ReCon can also display tax rebates and other data to benefit the client. ReCon will have a profound impact in the future of the fight against climate change. Our solution uses software to bypass the traditionally costly consultancy which is one of the many factors why renewable resources are so inaccessible to the economically disadvantaged. ReCon will affect the lives of people from all walks of life and shift the tides against climate change.</h3>
        </div>
      </main>

      {/* <footer className={styles.footer}>
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
      </footer> */}
    </div>
  )
}

