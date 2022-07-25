import Link from 'next/link'
import styles from '../styles/Home.module.css'
// import 'animate.css';

const Nav = () =>{
    return(
        <nav style={{ position: 'fixed', top: 0 }} className={styles.nav}>
            <ul className={styles.ul}>
                <li className={styles.li}>
                    <Link href='/'>Home</Link>
                </li>
                <li className={styles.li}>
                    <Link href='/application'>Consult</Link>
                </li>
            </ul>
        </nav>
    )
}
export default Nav
