<script>
  import { metatags } from "@roxi/routify";

  metatags.title = "ByeBee";
  metatags.description = "Description coming soon...";
  window.onscroll = function() {scrollFunction()};


</script>
<link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>

<header>
    <a href="#" class="logo"><img src="public/2.jpg" alt=""/></a>
    <ul class="navmenu">
        <li><a href="#">Home</a></li>
        <li><a href="#">Shop</a></li>
        <li><a href="#">Products</a></li>
        <li><a href="#">Review</a></li>
        <li><a href="#">Contact</a></li>
        <li><a href="#">Blogs</a></li>
    </ul> 
    <div class="nav-icon">
        <a href="#"><i class="bx bx-search"></i></a>
        <a href="#"><i class="bx bx-user"></i></a>
        <a href="#"><i class="bx bx-cart"></i></a>
        <div class="bx bx-menu" id="menu-icon"></div>
    </div>
</header>

<section id="hero">
  <div class="hero container">
    <div>
      <h1>Welcome</h1>
      <a href="#" type="button" class="cta">SHOP NOW</a>
    </div>
  </div>
</section>

<!-- <p>
    To see an example app that shows off a lot of Routify's features, go to <a href="/example">/example</a>
</p> -->
<style>
  *{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    scroll-behavior: smooth;
    font-family: sans-serif;
    list-style: none;
    text-decoration: none;
  }
  .navmenu{
    display: flex;

  }
  .navmenu a{
    color: white;
    font-size: 16px;
    text-transform: capitalize;
    padding: 10px 20px;
    font-weight: 400;
    transition: all .42s ease;
  }
  .navmenu a:hover{
    color: red;

  }
  .nav-icon{
    display: flex;
    align-items: center;
  }
  .nav-icon i{
    margin-right:20px;
    color: white;
    font-size:25px;
    font-weight : 400;
    transition: all .42s ease;
  }
  .nav-icon i:hover{
    transform:(1.1);
    color: red;
  }
  .logo img{
    height: auto;
    margin-left: 30px;
    max-width: 120px;
  }
  #menu-icon{
    font-size:35px;
    color:white;
    z-index:1001;
    cursor: pointer;
  }
  header{
    position: fixed;
    width: 100%;
    top: 0;
    right: 0;
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 20px 10%;
  }
  .container{
    min-height: 100vh;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center; 
  }
 
  #hero {
    background-image: url(/public/1.jpg);
    background-size: cover;
    background-position: center;
    position: relative;
    overflow: hidden;
    z-index: 1;
  }

  #hero::after {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
    width: 100%;
    background-color: black;
    opacity: 0.7;
    z-index: -1;
  }
  #hero h1 {
    display: block;
    width: fit-content;
    font-size: 4rem;
    color: #ddd;
    text-align: center;
    position: relative;
    animation: text_reveal 0.5s ease forwards;
    animation-delay: 1.5s;
    z-index: 4;
  }
  
  #hero .cta {
    display: inline-block;
    padding: 10px 30px;
    color: white;
    background-color: transparent;
    border: 2px solid crimson;
    font-size: 2rem;
    text-transform: uppercase;
    letter-spacing: 0.1rem;
    margin-top: 30px;
    transition: 0.3s ease;
    transition-property: background-color, color;
  }
  #hero .cta:hover {
    color: white;
    background-color: crimson;
  }
</style>
