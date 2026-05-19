import { LinearGradient } from "expo-linear-gradient"
import { Link, router } from "expo-router"
import { useState } from "react"
import { Alert, Image, StyleSheet, Text, View } from "react-native"

import { Button } from "@/components/button"
import { Input } from "@/components/input"


export default function IndexPage() {
   const [email, setEmail] = useState("")
   const [password, setPassword] = useState(" ")


   const entrar = () => {

    if( !email.trim() || !password.trim()) {
        return Alert.alert ("Entrar","Preencha email e senha para entrar")
  
          }
            const regex = /@gmail\.com$/

    if (!regex.test(email)) {
        alert("Use um Gmail válido")
        return
    }
     router.push("/main")

   }



        //Alert.alert ("Entrar,Função de entrar acionada")
            //console.log(email, password)
    

    return(

<LinearGradient colors={['#000166', '#0002CC']} style={styles.container}>
     <View>
            <Image source={require("../assets/logonaope.png")} style={styles.image}/>
            <Text style={styles.title}>Olá!</Text>
            <Text style={styles.subtitle}>Bem vindo ao insecta! Seu novo app para aprender</Text>

                <View style={styles.form}>
                    <Text style={styles.suptext}>Email:</Text>
                    <Input 
                        placeholder=" " 
                        keyboardType="email-address" 
                        onChangeText={setEmail}
                        autoCapitalize="none"
                    />

                    <Text style={styles.suptext}>Senha:</Text>
                     <Input 
                        placeholder=" " 
                        secureTextEntry
                        onChangeText={setPassword}
                    />
                    <Text style={styles.footerText}> 
                        Esquceu a senha? Clique aqui!
                    </Text>
                    <Button 
                        label="Entrar"
                        onPress={entrar}
                    />
                </View>

            <Text style={styles.footerText}>

            Não tem uma conta? {" "}
            <Link href="/signup" style={styles.footerLink}>Crie aqui!</Link>

            </Text>

    </View>
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

    image: {
        width: 100,
        height: 100,
        position:"absolute",
        top: 65,
        marginLeft: 250
    },

    title: {
        color:'#fff',
        fontSize: 24,
        fontWeight: "bold" 
        
    },

    subtitle:{
        color:'#fff',
        fontSize: 18,
        fontWeight: "bold"
    },

    suptext:{
        color:'#fff',

    },
    
    form:{
        marginTop:24,
        gap: 12,
       
    },

    footerText:{
        color:"#fff",
        marginLeft:5

    },

    footerLink:{
        color:"#FFC43F",
        fontWeight: 700
     
    }


})

