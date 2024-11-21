
// for dark and light mode 
const darkmodebtn = document.querySelectorAll(".dark-light-mode")
// console.log(darkmodebtn);
const lightmode = document.querySelectorAll(".lightmodes")
const darkmode = document.querySelectorAll(".darkmodes")
console.log(lightmode[1]);
console.log(darkmode[1]);


darkmodebtn.forEach((data)=>{
    data.addEventListener("click",()=>{
        document.body.classList.toggle("darkmode")
        if(document.body.className === "darkmode"){
        darkmode.forEach((dm)=>{
            dm.style.display="none"
        })
        lightmode.forEach((lm)=>{
            lm.style.display="block"
        })


        // darkmode.style.display = "none"
        //     lightmode.style.display="block"
        }
        else{
            // darkmode.style.display = "block"
            // lightmode.style.display="none" 
            darkmode.forEach((dm)=>{
                dm.style.display="block"
            })
            lightmode.forEach((lm)=>{
                lm.style.display="none"
            })
    
        }
    })
})


// for responsive navbar 

const navbar = document.querySelector(".nav");
const closenavbar = document.querySelector(".close-navbar");

navbarStart.addEventListener("click", () => {
    navbar.classList.add("open");
});

closenavbar.addEventListener("click", () => {
    navbar.classList.remove("open");
});




// for project 

const viewbutton = document.querySelectorAll(".view-icon")
const overbox = document.querySelectorAll(".overlay-2")
// const overlaybox = document.querySelectorAll(".overlay-2")



viewbutton.forEach((btn,index) => {
    btn.addEventListener("mouseenter", (e) => {
        console.log(e.target);
        
        overbox.forEach((box,index2) => {
            console.log(box);
if(index === index2){
    box.style.transition = "top 0.3s ease"; // Optional: for smooth animation
    box.style.top = "0px"; // Slide in from the top
}

            
           
               
         
              
           
        });
    });

    // btn.addEventListener("mouseleave", () => {
    //     overbox.forEach((box) => {
    //         box.style.transition = "top 0.3s ease"; // Optional: for smooth animation
    //         box.style.top = "100%"; // Slide out to hide
    //     });
    // });
});

overbox.forEach((overbox)=>{
    overbox.addEventListener("mouseleave",()=>{
        overbox.style.transition = "top 0.3s ease"; // Optional: for smooth animation
        overbox.style.top= "100%"
    })
})