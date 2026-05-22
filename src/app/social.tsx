import { LinearGradient } from "expo-linear-gradient"
import { Link } from "expo-router"
import { Alert, Image, StyleSheet, TouchableOpacity, View } from "react-native"




export default function IndexPage() {
    const Iniciar = () => {
        Alert.alert(":(","Não temos níveis disponíveis!")

    }

    return(

<LinearGradient colors={['#000166', '#0002CC']} style={styles.container}>
    <View style={styles.upBar}></View>

    <View style={styles.downBar}></View>
         <TouchableOpacity onPress={() => alert("Página indisponível no momento")}><Link href="/social" style={styles.socialL}><Image source={require("../assets/users-alt (1).png")} style={styles.social}/></Link></TouchableOpacity>
        <Link href="/main" style={styles.homeL}><Image source={require("../assets/home (1).png")} style={styles.home}/></Link>
        <Link href="/user" style={styles.userL}><Image source={require("../assets/user (1).png")} style={styles.user}/></Link>
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

    upBar: {
        backgroundColor:"black",
        padding: 70,
        borderRadius: 10,
        position:"absolute",
        marginBottom: 800,
        width:500

    },


    social:{
        width:35,
        height:35
    },

    socialL:{
    position:"absolute",
    marginRight:200,
    marginTop:750
    },

    home:{
        width:30,
        height:30,

    },

    homeL:{
    position:"absolute",
    marginTop:750
    },

    user:{
        width:30,
        height:30
    },

    userL:{
    position:"absolute",
    marginLeft:200,
    marginTop:750
    },

    downBar: {
    backgroundColor:"black",
    padding: 50,
    borderRadius: 10,        position:"absolute",
    marginTop: 800,
    width:500



        
        
    },
    
    },



)