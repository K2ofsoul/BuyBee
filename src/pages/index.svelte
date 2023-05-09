<script>
  import { metatags } from "@roxi/routify";

  metatags.title = "ByeBee";
  metatags.description = "Description coming soon...";
  window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.querySelector('.social-bar').style.display = 'block';
  } else {
    document.querySelector('.social-bar').style.display = 'none';
  }
}

</script>

<nav>
  <a href="#" class="logo"><img src="public/2.jpg" alt=""/></a>
  <a href="#">Buy Bee</a>
  <a href="#" class="active">Shop</a>
  <a href="#">About</a>
  <a href="#">Forum</a>
  <a href="#">Contact</a>
  <a href="#">Search</a>
  <a href="#">Login</a>
  <a href="#">Cart Shopping</a>
</nav>
<div class="social-bar">
  <a href="#"><i class="fab fa-facebook-f"></i></a>
  <a href="#"><i class="fab fa-instagram"></i></a>
  <a href="#"><i class="fab fa-github"></i></a>
</div>

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
  nav {
    position: fixed;
    background-color: #333;
    overflow: hidden;
    height: 50px;
    top: 0;
    width: 100%;
    z-index: 999;
  }
  .logo img{
    height: 30px;
    width: 30px;
    margin-left: 30px;
  }
  .logo a{
    justify-content: center;
  }
  .active{
    margin-left: 600px;
  }
  nav a {
    float: left;
    color: white;
    text-align: center;
    padding: 16px 18px;
    text-decoration: none;
    font-size: 18px;
    font-weight: bold;
  }

  nav a.active {
    background-color: #4caf50;
  }
  nav a:hover {
    background-color: #ddd;
    color: black;
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
  .social-bar {
  position: fixed;
  top: 50%;
  right: 0;
  transform: translateY(-50%);
  display: flex;
  flex-direction: column;
  z-index: 30;
}

.social-bar a {
  color: white;
  font-size: 20px;
  margin-bottom: 10px;
  text-decoration: none;
  transition: all 0.2s ease-in-out;
}

.social-bar a:hover {
  transform: scale(1.1);
}

</style>
