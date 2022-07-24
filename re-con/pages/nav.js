import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'
import styles from '../styles/Home.module.css'

const Nav = () =>{
    return(
        <nav className={styles.nav}>
            <ul className={styles.ul}>
                <li>
                    <img src="ReCon(1).png"></img>
                </li>
                <li className={styles.li}>
                    <Link href='/'>Home</Link>
                </li>
                <li className={styles.li}>
                    <Link href='/about'>About</Link>
                </li>
                <li className={styles.li}>
                    <Link href='/application'>Consult</Link>
                </li>
            </ul>
        </nav>
    )
}
export default Nav
