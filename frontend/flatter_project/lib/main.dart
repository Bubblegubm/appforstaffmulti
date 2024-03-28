import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      // This call to setState tells the Flutter framework that something has
      // changed in this State, which causes it to rerun the build method below
      // so that the display can reflect the updated values. If we changed
      // _counter without calling setState(), then the build method would not be
      // called again, and so nothing would appear to happen.
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [
              Color(0xFF3300FF),
              Color(0xFFBD00FF),
            ],
          ),
        ),
        child: Scaffold(
          backgroundColor: Colors.transparent, // Делаем фон Scaffold прозрачным
          body: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                FittedBox(
                  fit: BoxFit.contain, // Или BoxFit.cover для заполнения всего пространства
                  child: Image.asset('assets/logo.png'),
                ),
                Text(
                  'ServeSmart',
                  style: TextStyle(
                    fontFamily: 'jsMath-cmbx10',
                    fontStyle: FontStyle.normal,
                    fontWeight: FontWeight.bold,
                    fontSize: 40.0,
                    height: 1.09,
                    color: Colors.white,
                    shadows: [
                      Shadow(
                        blurRadius: 1.0,
                        offset: Offset(2.0, 3.0),
                        color: Colors.black.withOpacity(0.5),
                      ),
                    ],
                  ),
                ),
                Column(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: <Widget>[
                    ElevatedButton(
                      onPressed: () {},
                      style: ElevatedButton.styleFrom(
                        padding: EdgeInsets.zero,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(15),
                          side: BorderSide(
                            color: Colors.white, // Полупрозрачный белый цвет границы
                            width: 2.0, // Толщина границы
                          ),
                        ),
                        elevation: 10, // Высота тени
                        // shadowColor: Colors.black, // Цвет тени
                        backgroundColor: Colors.white.withOpacity(0.2), // Полупрозрачный белый цвет фона
                      ),
                      child: Container(
                        width: 230,
                        height: 50,
                        child: Center(
                          child: Text(
                            'Вход',
                            style: TextStyle(
                              fontFamily: 'jsMath-cmbx10',
                              fontStyle: FontStyle.normal,
                              fontWeight: FontWeight.bold,
                              fontSize: 25.0,
                              height: -0.30,
                              color: Colors.white,
                            ),
                          ),
                        ),
                      ),
                    ),
                    ElevatedButton(
                      onPressed: () {},
                      style: ElevatedButton.styleFrom(
                        padding: EdgeInsets.zero,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(15),
                          side: BorderSide(
                            color: Colors.white, // Полупрозрачный белый цвет границы
                            width: 2.0, // Толщина границы
                          ),
                        ),
                        elevation: 10, // Высота тени
                        // shadowColor: Colors.black, // Цвет тени
                        backgroundColor: Colors.white.withOpacity(0.2), // Полупрозрачный белый цвет фона
                      ),
                      child: Container(
                        width: 230,
                        height: 50,
                        child: Center(
                          child: Text(
                            'Регистрация',
                            style: TextStyle(
                              fontFamily: 'jsMath-cmbx10',
                              fontStyle: FontStyle.normal,
                              fontWeight: FontWeight.bold,
                              fontSize: 25.0,
                              height: -0.30,
                              color: Colors.white,
                            ),
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
