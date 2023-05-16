<script>
  import { metatags } from "@roxi/routify";

  metatags.title = "ByeBee";
  metatags.description = "Description coming soon...";
  window.onscroll = function () {
    scrollFunction();
  };
  const header = document.querySelector("header");
  window.addEventListener("scroll", function () {
    header.chatList.toogle("sticky", this.window.scrollY > 0);
  });
</script>

<link
  href="https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css"
  rel="stylesheet"
/>

<header class="sticky">
  <a href="#logo" class="logo"><img src="public/2.jpg" alt="" /></a>
  <ul class="navmenu">
    <li><a href="#home">Home</a></li>
    <li><a href="#shop">Shop</a></li>
    <li><a href="#product">Products</a></li>
    <li><a href="#review">Review</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#blogs">Blogs</a></li>
  </ul>
  <div class="nav-icon">
    <a href="#search"><i class="bx bx-search" /></a>
    <a href="#user"><i class="bx bx-user" /></a>
    <a href="#cart"><i class="bx bx-cart" /></a>
    <div class="bx bx-menu" id="menu-icon" />
  </div>
</header>

<section id="hero">
  <div class="hero container">
    <div>
      <h1>Welcome</h1>
      <a href="#shopnow" type="button" class="cta"
        >SHOP NOW <i class="bx bx-right-arrow-alt" /></a
      >
    </div>
  </div>
  <div class="down-arrow">
    <a href="#trending" class="down"><i class="bx bx-down-arrow-alt" /></a>
  </div>
</section>
<section class="trending-product" id="trending">
  <div class="center-text">
    <h2>Our Trending <span>Products</span></h2>
  </div>
  <div class="products">
    <!-- firstproduct -->
    <div class="row">
      <img src="/public/laptop/1.jpg" alt="" />

      <div class="product-text">
        <h5>HOT</h5>
      </div>
      <div class="heart-icon">
        <i class="bx bx-heart" />
      </div>
      <div class="ratting">
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bxs-star-half" />
      </div>
      <div class="price">
        <h4>13-inch Macbook Air</h4>
        <p>$37,900</p>
      </div>
    </div>
    <!-- secondproduct -->
    <div class="row">
      <img src="/public/laptop/2.jpg" alt="" />

      <div class="product-text">
        <h5>Sale</h5>
      </div>
      <div class="heart-icon">
        <i class="bx bx-heart" />
      </div>
      <div class="ratting">
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bxs-star-half" />
      </div>
      <div class="price">
        <h4>Macbook Pro13</h4>
        <p>$37,500</p>

      </div>
    </div>
    <!-- thirdproduct -->
    <div class="row">
      <img src="/public/phone/1.jpg" alt="" />

      <div class="product-text">
        <h5>NEW</h5>
      </div>
      <div class="heart-icon">
        <i class="bx bx-heart" />
      </div>
      <div class="ratting">
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bxs-star-half" />
      </div>
      <div class="price">
        <h4>Apple iPhone 14 Pro</h4>
        <p>$32,888</p>
      </div>
    </div>
    <!-- fourproduct -->
    <div class="row">
      <img src="/public/phone/2.jpg" alt="" />

      <div class="product-text">
        <h5>Sale</h5>
      </div>
      <div class="heart-icon">
        <i class="bx bx-heart" />
      </div>
      <div class="ratting">
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bxs-star-half" />
      </div>
      <div class="price">
        <h4>Apple iPhone 14 Plus</h4>
        <p>$29,388</p>
      </div>
    </div>
    <!-- fifthproduct -->
    <div class="row">
      <img src="/public/tablet/1.jpg" alt="" />

      <div class="product-text">
        <h5>Sale</h5>
      </div>
      <div class="heart-icon">
        <i class="bx bx-heart" />
      </div>
      <div class="ratting">
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bxs-star-half" />
      </div>
      <div class="price">
        <h4>Apple iPad 10.2</h4>
        <p>$10,355</p>
      </div>
    </div>
    <!-- sixproduct -->
    <div class="row">
      <img src="/public/tablet/2.jpg" alt="" />
      <div class="product-text">
        <h5>NEW</h5>
      </div>
      <div class="heart-icon">
        <i class="bx bx-heart" />
      </div>
      <div class="ratting">
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bx-star" />
        <i class="bx bxs-star-half" />
      </div>
      text-decoration: none;
      <div class="price">
        <h4>2022 Apple iPad 10.9</h4>
        <p>$18,199</p>
      </div>
    </div>
  </div>
</section>
<!-- Review Section -->
<section class="client-section">
    <div class="review">
      <h3>Client Reviews</h3>
      <img src="" alt="">
      <p></p>
      <h2></h2>
      <p></p>
    </div>
</section>
<!-- <p>
    To see an example app that shows off a lot of Routify's features, go to <a href="/example">/example</a>
</p> -->
<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    scroll-behavior: smooth;
    font-family: sans-serif;
    list-style: none;
  }
  header {
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
  .navmenu {
    display: flex;
  }
  .navmenu a {
    color: white;
    font-size: 16px;
    text-transform: capitalize;
    padding: 10px 20px;
    font-weight: 400;
    transition: all 0.42s ease;
  }
  .navmenu a:hover {
    color: red;
  }
  .nav-icon {
    display: flex;
    align-items: center;
  }
  .nav-icon i {
    margin-right: 20px;
    color: white;
    font-size: 25px;
    font-weight: 400;
    transition: all 0.42s ease;
  }
  .nav-icon i:hover {
    transform: (1.1);
    color: red;
  }
  .logo img {
    height: auto;
    margin-left: 30px;
    max-width: 120px;
  }
  #menu-icon {
    font-size: 35px;
    color: white;
    z-index: 1001;
    cursor: pointer;
  }

  .container {
    min-height: 100vh;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  #hero {
    background-image: url(/public/4.jpg);
    background-size: cover;
    background-position: center;
    position: relative;
    overflow: hidden;
    z-index: 1;
    width: 100%;
    height: 100vh;
    display: grid;
    grid-template-columns: repeat(1, 1 fr);
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
  .down-arrow {
    position: absolute;
    top: 85%;
    right: 10%;
  }
  .down i {
    color: white;
    font-size: 30px;
    border: 2px solid white;
    border-radius: 50%;
    padding: 12px 12px;
  }
  .down i:hover {
    background-color: #ddd;
    color: black;
    transform: all 0.42s ease;
  }
  header.sticky {
    background-color: black;
    padding: 20px 10%;
    box-shadow: 0 0 10px rgb(0, 0, 0/10%);
  }
  /* trending section */
  .center-text h2 {
    padding: 50px;
    color: black;
    font-size: 28px;
    text-transform: capitalize;
    text-align: center;
  }
  .center-text span {
    color: red;
  }
  .products {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, auto));
    gap: 2rem;
  }
  .row {
    position: relative;
    transition: all 0.4s;
  }
  .row img {
    width: 100%;
    height: auto;
    transition: all 0.4s;
  }
  .row img:hover {
    transform: scale(0.9);
  }
  .product-text h5{
    position: absolute;
    top: 13px;
    left: 13px;
    color: white;
    font-size: 12px;
    font-weight:500;
    text-transform: uppercase;
    background-color: #27b737;
    padding: 3px 10px;
    border-radius: 2px;
  }
  .heart-icon{
    position: absolute;
    right:0;
    font-size: 20px;
  }
  .heart-icon:hover{
    color:red;
  }
  .ratting {
    color: #FF8C00;
    font-size: 18px;
  }
  .price h4{
    color: black;
    font-size: 16px;
    text-transform: capitalize;
    font-size: 400;
  }
  .price p{
    color: black;
    font-size: 14px;
    font-weight: 600;
  }
</style>
