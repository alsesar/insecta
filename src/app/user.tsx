import { LinearGradient } from "expo-linear-gradient"
import { Link } from "expo-router"
import { Image, StyleSheet, View } from "react-native"




export default function IndexPage() {

    return(

<LinearGradient colors={['#000166', '#0002CC']} style={styles.container}>

    <View style={styles.up}></View>
    <View style={styles.down}></View>
            <Link href="/user" style={styles.userL}><Image source={require("../assets/user.png")} style={styles.user} /></Link>
            <Link href="/main" style={styles.homeL}><Image source={require("../assets/home.png")} style={styles.home}/></Link>
            <Image source={require("../assets/group.png")} style={styles.group}/>

</LinearGradient>
    
   

)
}

const styles = StyleSheet.create({

    container: {
        flex: 1,
        justifyContent:"center",
        alignItems:"center",
        padding: 20


    },


    up: {
        backgroundColor: '#484848',
        opacity:0.7,
        position:"absolute",
        marginBottom:800,
        width:400,
        padding:70,
        borderRadius:50
    },

    down: {
        backgroundColor: '#484848',
        opacity:0.7,
        position:"absolute",
        marginTop:800,
        width:400,
        padding:50,
        borderRadius:50
    },

    user:{
        width:30,
        height:30,
        position:"absolute",
        marginTop:750,
        marginLeft:200
    },


    userL:{
        position:"absolute",
        marginTop:750,
        marginLeft:200

    },


    home:{
        width:30,
        height:30,


    },

    homeL:{
        position:"absolute",
        marginTop:750,

    },

    group:{
        width:40,
        height:40,
        position:"absolute",
        marginTop:750,
        marginRight:200
    },

    title: {
        color:'#fff',
        fontSize: 24,
        fontWeight: "bold",
        position:"absolute",
        marginBottom:350
        
    },

    subtitle:{
        color:'#fff',
        fontSize: 18,
        position:"absolute",
        marginBottom:250,
        marginRight:50

    },

    subtitle1:{
        color:'#fff',
        fontSize: 18,
        position:"absolute",
        marginBottom:175,
        marginRight:100

    },

    subtitle2:{
        color:'#fff',
        fontSize: 15,
        position:"absolute",
        marginBottom:100,
        marginLeft:80


    },


})

