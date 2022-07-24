import styles from '../styles/Home.module.css'

export const layout = ({children}) => {
  return (
    <div className={styles.container}>
        <main className={styles.main}>
            {children}
        </main>
    </div>
  )
}
