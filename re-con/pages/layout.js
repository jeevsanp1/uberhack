import styles from '../styles/Home.module.css'
import 'animate.css';

export const layout = ({children}) => {
  return (
    <div className={styles.container}>
        <main className={styles.main}>
            {children}
        </main>
    </div>
  )
}
