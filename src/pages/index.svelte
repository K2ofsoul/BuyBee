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
  <a href="#logo" class="logo"><img src="public/logo.jpg" alt="" /></a>
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
    <img src="/public/client/1.jpg" alt="" />
    <p>
      Arrived quickly and by all appearances is a brand new item. Manual very
      simple. I removed packing material, set it on the floor, plugged it in and
      turned it on. Have it set on low setting and its air flow is noticeably
      keeping my home cooler. Hopefully will notice a savings in my electric
      bill. Have not been using my dehumidifier as often since I plugged in this
      fan. One person found this helpful
    </p>
    <h2>Quinton</h2>
  </div>
</section>
<!-- update-new-section -->
<section class="update-news">
  <div class="up-center-text">
    <h2>New updates</h2>
  </div>
  <div class="update-cart">
    <div class="cart">
      <img src="/public/news/1.webp" alt="" />
      <h5>16 may 2023</h5>
      <h4>Microsoft's Activision takeover approved by EU after UK veto</h4>
      <p>
        U regulators have approved Microsoft's $69bn (£55bn) attempt to purchase
        Call of Duty publisher Activision Blizzard. The European Commission (EC)
        said Microsoft had addressed their concerns on competition issues. It
        comes three weeks after the UK blocked the deal over worries it would
        hurt competition in the emerging cloud gaming business. The proposed
        takeover is poised to be the biggest deal in gaming history but has
        split global regulators. In order for the deal to go through Microsoft
        and Activision need approval from regulatory bodies in the UK, EU and
        the US. The US Federal Trace Commission filed a lawsuit in December to
        block the deal - a judge's decision is unlikely before the end of the
        year.
      </p>
      <h6>Continue Reading...</h6>
    </div>
    <div class="cart">
      <img src="/public/news/2.webp" alt="" />
      <h5>16 may 2023</h5>
      <h4>Online depression therapy given go-ahead in England</h4>
      <p>
        Nine online talking-therapy treatments for anxiety or depression have
        been given the green light to be used by the NHS in England. They
        offered faster access to help but less time with a therapist, which may
        not suit everyone, the health body recommending them said. There is huge
        demand for face-to-face services, with people waiting several weeks to
        see a therapist. Psychiatrists said digital therapies were not a
        long-term solution. Mental-health charity Sane said they were no
        substitute for a one-to-one relationship and could leave people feeling
        even more isolated than before.
      </p>
      <h6>Continue Reading...</h6>
    </div>
    <div class="cart">
      <img src="/public/news/3.webp" alt="" />
      <h5>16 may 2023</h5>
      <h4>Google reveals AI updates as it vies with Microsoft</h4>
      <p>
        Google has announced it is rolling out generative artificial
        intelligence (AI) to its core search engine. The move comes after
        Microsoft incorporated GPT-4 into its Bing search engine earlier this
        year. Search Generative Experience - which will be part of Google - will
        craft responses to open-ended queries, the company said. However, the
        system will only be available to a limited number of users and is still
        in "experimental" phase. "We are reimagining all of our core products,
        including search," said Sundar Pichai, the boss of Google's parent
        company Alphabet. Additionally, the company announced a new feature on
        Google's Android system will proactively warn users about unknown
        AirTags, tiny devices developed to track personal items like keys and
        wallets.
      </p>
      <h6>Continue Reading...</h6>
    </div>
  </div>
</section>
<!-- contact section -->
<section class="contact">
  <div class="contact-info">
    <div class="first-info">
      <img src="/public/logo.jpg" alt="" />
      <p>zhongshan road douliu city yunlin county taiwan</p>
      <p>0912345678</p>
      <p>123@gmail.com</p>
      <div class="social-icon">
        <a href="#"><i class="bx bxl-facebook" /></a>
        <a href="#"><i class="bx bxl-instagram" /></a>
        <a href="#"><i class="bx bxl-twitter" /></a>
        <a href="#"><i class="bx bxl-youtube" /></a>
        <a href="#"><i class="bx bxl-linkedin" /></a>
      </div>
    </div>
    <div class="second-info">
      <h4>Support</h4>
      <p>Contact us</p>
      <p>About page</p>
      <p>Size Guide</p>
      <p>Shopping & Returns</p>
      <p>Privacy</p>
    </div>
    <div class="third-info">
      <h4>Shop</h4>
      <p>Fashion</p>
      <p>Sports$motors</p>
      <p>Electronics</p>
      <p>Life Style</p>
    </div>
    <div class="fourth-info">
      <h4>Company</h4>
      <p>About</p>
      <p>Blog</p>
      <p>VIP client</p>
      <p>Login</p>
    </div>
  </div>
</section>
<div class="end-text">
  <p>Copyright @2023. All Rights Reversed</p>
</div>

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
  .product-text h5 {
    position: absolute;
    top: 13px;
    left: 13px;
    color: white;
    font-size: 12px;
    font-weight: 500;
    text-transform: uppercase;
    background-color: #27b737;
    padding: 3px 10px;
    border-radius: 2px;
  }
  .heart-icon {
    position: absolute;
    right: 0;
    font-size: 20px;
  }
  .heart-icon:hover {
    color: red;
  }
  .ratting {
    color: #ff8c00;
    font-size: 18px;
  }
  .price h4 {
    color: black;
    font-size: 16px;
    text-transform: capitalize;
    font-size: 400;
  }
  .price p {
    color: black;
    font-size: 14px;
    font-weight: 600;
  }
  .client-section {
    background-color: #f3f4f6;
  }
  .review {
    text-align: center;
  }
  .review h3 {
    color: black;
    text-transform: capitalize;
    text-align: center;
    font-weight: 700;
    font-size: 30px;
    padding: 20px;
  }
  .review img {
    width: 150px;
    height: auto;
    border-radius: 50px;
    margin: 10px 0;
  }
  .review p {
    color: #707070;
    font-size: 16px;
    font-weight: 400;
    line-height: 25px;
    margin-bottom: 10px;
  }
  .review h2 {
    color: black;
    font-size: 22px;
    font-weight: 400;
    text-transform: capitalize;
    margin-bottom: 2px;
  }
  .up-center-text h2 {
    text-align: center;
    color: black;
    font-size: 25px;
    text-transform: capitalize;
    font-weight: 700;
    margin-bottom: 30px;
  }
  .cart img {
    width: 450px;
    height: auto;
    border-radius: 5px;
  }
  .update-cart {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, auto));
    gap: 1rem;
  }
  .cart h5 {
    color: black;
    font-size: 14px;
    text-transform: capitalize;
    font-weight: 500;
  }
  .cart h4 {
    color: black;
    font-size: 18px;
    font-weight: 600;
  }
  .cart p {
    color: #707070;
    font-size: 15px;
    max-width: 500px;
    line-height: 25px;
    margin-bottom: 12px;
  }
  .cart h6 {
    color: black;
    font-size: 14px;
    font-weight: 500;
  }
  /* Contact section */
  .contact {
    background-color: #f3f4f6;
  }
  .contact-info {
    padding: 30px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, auto));
    gap: 2rem;
  }
  .first-info img {
    width: 140px;
    height: auto;
  }
  .contact-info h4 {
    color: #212529;
    font-size: 14px;
    text-transform: uppercase;
    margin-bottom: 10px;
  }
  .contact-info p {
    color: #565656;
    font-size: 14px;
    font-weight: 400;
    text-transform: capitalize;
    line-height: 1.5;
    margin-bottom: 10px;
    cursor: pointer;
    transition: all 0.42s;
  }
  .contact-info p:hover {
    color: red;
  }
  .social-icon i {
    color: #565656;
    margin-right: 10px;
    font-size: 20px;
    transition: all 0.42s;
  }
  .social-icon i:hover {
    transform: scale(1.3);
  }
  .end-text {
    background-color: white;
    text-align: center;
    padding: 20px;
  }
  .end-text p {
    color: black;
    text-transform: capitalize;
  }
  @media (max-width: 890px) {
    header {
      padding: 20px 3%;
      transition: 0.4s;
    }
  }
  @media (max-width: 600px) {
    .hero container h1 {
      font-size: 50px;
      transition: 0.4s;
    }
  }
  @media (max-width: 750px) {
    .navmenu {
      position: absolute;
      top: 100%;
      right: 0;
      width: 300px;
      height: 130vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 120px 30px;
      transition: all 0.42s;
    }
  }
</style>
