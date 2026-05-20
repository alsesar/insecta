import { LinearGradient } from "expo-linear-gradient"
import { Link } from "expo-router"
import { Alert, Image, StyleSheet, Text, View } from "react-native"

import { Button } from "@/components/button"



export default function IndexPage() {
    const iniciar = () => {
        return Alert.alert (":(","Não temos atividades disponíveis pro seu nível")
    }



    return(

<LinearGradient colors={['#000166', '#0002CC']} style={styles.container}>
    <View style={styles.card}></View>
    <View style={styles.up}></View>
    <View style={styles.down}></View>
    <View style={styles.mid}></View>
            <Image source={require("../assets/patchdourado1.png")} style={styles.coin}/>
            <Image source={require("../assets/logoempeolhofechado.png")} style={styles.joana1}/>
            <Link href="/user" style={styles.userL}><Image source={require("../assets/user.png")} style={styles.user} /></Link>
            <Image source={require("../assets/home.png")} style={styles.home}/>
            <Image source={require("../assets/group.png")} style={styles.group}/>
            <Image source={require("../assets/avancadolinha.png")} style={styles.level}/>
            <Image source={require("../assets/next.png")} style={styles.next} />
                <Button style={styles.button}
                label="Iniciar" 
                onPress={iniciar} 
                />
                <Text style={styles.title}>Exercício 1</Text>
                <Text style={styles.subtitle}>Nível:</Text>
                <Text style={styles.subtitle1}>Descrição:</Text>
                <Text style={styles.subtitle2}>Relacione as imagens aos seus correspondentes!</Text>
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

    card: {
        backgroundColor: '#484848',
        opacity:0.7,
        padding: 150,
        borderRadius: 30,
        position:"absolute",
        marginBottom:30,
        height: 400


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

    mid: {
        backgroundColor: '#484848',
        opacity:0.7,
        position:"absolute",
        padding:55,
        borderRadius:30,
        marginBottom:320,
        width:300,
    

    },


    coin: {
        width: 120,
        height: 120,
        position:"absolute",
        marginRight:230,
        marginBottom:350
        
    },

    joana1:{
        width: 200,
        height: 200,
        position: "absolute",
        marginRight:200,
        marginTop:190

    },

    level:{
        width: 50,
        height: 50,
        position: "absolute",
        marginBottom:250,
        marginLeft:50


    },

    next:{
        width: 30,
        height: 30,
        opacity: 0.5,
        position: "absolute",
        marginBottom:100,
        marginLeft:350


    },


    button: {
        width: 300,
        height: 48,
        borderRadius: 8,
        backgroundColor:"#FFC43F",
        marginTop:450

    },

    user:{
        width:30,
        height:30,

    },

    userL:{
        position:"absolute",
        marginTop:750,
        marginLeft:200

    },

    home:{
        width:30,
        height:30,
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

