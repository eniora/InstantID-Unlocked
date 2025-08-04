style_list = [
    {
        "name": "(No style)",
        "prompt": "{prompt}",
        "negative_prompt": "",
    },
    {
        "name": "Photographic",
        "prompt": "cinematic photo {prompt}. 35mm photograph, film, bokeh, professional, 4k, highly detailed",
        "negative_prompt": "drawing, painting, crayon, sketch, graphite, impressionist, noisy, blurry, soft, deformed, ugly",
    },
    {
        "name": "Film Noir",
        "prompt": "film noir style, ink sketch|vector, {prompt} highly detailed, sharp focus, ultra sharpness, monochrome, high contrast, dramatic shadows, 1940s style, mysterious, cinematic",
        "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, blurry, deformed cat, deformed photo",
    },
    {
        "name": "Neon",
        "prompt": "masterpiece painting, buildings in the backdrop, kaleidoscope, lilac orange blue cream fuchsia bright vivid gradient colors, the scene is cinematic, {prompt}, emotional realism, double exposure, watercolor ink pencil, graded wash, color layering, magic realism, figurative painting, intricate motifs, organic tracery, polished",
        "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, blurry, deformed cat, deformed photo",
    },
    {
        "name": "Jungle",
        "prompt": 'waist-up "{prompt} in a Jungle" by Syd Mead, tangerine cold color palette, muted colors, detailed, 8k,photo r3al,dripping paint,3d toon style,3d style,Movie Still',
        "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, blurry, deformed cat, deformed photo",
    },
    {
        "name": "Mars",
        "prompt": "{prompt}, Post-apocalyptic. Mars Colony, Scavengers roam the wastelands searching for valuable resources, rovers, bright morning sunlight shining, (detailed) (intricate) (8k) (HDR) (cinematic lighting) (sharp focus)",
        "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, blurry, deformed cat, deformed photo",
    },
    {
        "name": "Vibrant Color",
        "prompt": "vibrant colorful, ink sketch|vector|2d colors, at nightfall, sharp focus, {prompt}, highly detailed, sharp focus, the clouds,colorful,ultra sharpness",
        "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, blurry, deformed cat, deformed photo",
    },
    {
        "name": "Snow",
        "prompt": "cinema 4d render, {prompt}, high contrast, vibrant and saturated, sico style, surrounded by magical glow,floating ice shards, snow crystals, cold, windy background, frozen natural landscape in background  cinematic atmosphere,highly detailed, sharp focus, intricate design, 3d, unreal engine, octane render, CG best quality, highres, photorealistic, dramatic lighting, artstation, concept art, cinematic, epic Steven Spielberg movie still, sharp focus, smoke, sparks, art by pascal blanche and greg rutkowski and repin, trending on artstation, hyperrealism painting, matte painting, 4k resolution",
        "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, blurry, deformed cat, deformed photo",
    },
    {
        "name": "Line art",
        "prompt": "line art drawing {prompt}. professional, sleek, modern, minimalist, graphic, line art, vector graphics",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, blurry, noisy, off-center, deformed, cross-eyed, closed eyes, bad anatomy, ugly, disfigured, mutated, realism, realistic, impressionism, expressionism, oil, acrylic",
    },
    {
        "name": "Cinematic",
        "prompt": "cinematic still {prompt}. emotional, harmonious, vignette, highly detailed, high budget, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy",
        "negative_prompt": "anime, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured",
    },
    {
        "name": "Disney Charactor",
        "prompt": "A Pixar animation character of {prompt}. pixar-style, studio anime, Disney, high-quality",
        "negative_prompt": "lowres, bad anatomy, bad hands, text, bad eyes, bad arms, bad legs, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, blurry, grayscale, noisy, sloppy, messy, grainy, highly detailed, ultra textured, photo",
    },
    {
        "name": "Neonpunk",
        "prompt": "neonpunk style {prompt}. cyberpunk, vaporwave, neon, vibes, vibrant, stunningly beautiful, crisp, detailed, sleek, ultramodern, magenta highlights, dark purple shadows, high contrast, cinematic, ultra detailed, intricate, professional",
        "negative_prompt": "painting, drawing, illustration, glitch, deformed, mutated, cross-eyed, ugly, disfigured",
    },
    {
        "name": "Comic Book",
        "prompt": "comic {prompt}. graphic illustration, comic art, graphic novel art, vibrant, highly detailed",
        "negative_prompt": "photograph, deformed, glitch, noisy, realistic, stock photo",
    },
    {
        "name": "Abstract",
        "prompt": "Abstract style art of {prompt}, Non-representational, colors and shapes, expression of feelings, imaginative, highly detailed",
        "negative_prompt": "realistic, photographic, figurative, concrete"
    },
    {
        "name": "Abstract Expressionism",
        "prompt": "abstract expressionist painting of {prompt}, energetic brushwork, bold colors, abstract forms, expressive, emotional",
        "negative_prompt": "realistic, photorealistic, low contrast, plain, simple, monochrome"
    },
    {
        "name": "Adorable 3D Character",
        "prompt": "Adorable 3D Character of {prompt}, 3D render, adorable character, 3D art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, grunge, sloppy, unkempt, photograph, photo, realistic"
    },
    {
        "name": "Adorable Kawaii",
        "prompt": "Adorable Kawaii, {prompt}, pretty, cute, adorable, kawaii",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, gothic, dark, moody, monochromatic"
    },
    {
        "name": "Advertising",
        "prompt": "Advertising poster style, {prompt}, Professional, modern, product-focused, commercial, eye-catching, highly detailed",
        "negative_prompt": "noisy, blurry, amateurish, sloppy, unattractive"
    },
    {
        "name": "Alien",
        "prompt": "Alien-themed {prompt}, Extraterrestrial, cosmic, otherworldly, mysterious, sci-fi, highly detailed",
        "negative_prompt": "earthly, mundane, common, realistic, simple"
    },
    {
        "name": "Anime",
        "prompt": "anime artwork of {prompt}, anime style, key visual, vibrant, studio anime,  highly detailed",
        "negative_prompt": "photo, deformed, black and white, realism, disfigured, low contrast"
    },
    {
        "name": "Architectural",
        "prompt": "Architectural style, {prompt}, Clean lines, geometric shapes, minimalist, modern, architectural drawing, highly detailed",
        "negative_prompt": "curved lines, ornate, baroque, abstract, grunge"
    },
    {
        "name": "Art Deco",
        "prompt": "art deco style, {prompt}, geometric shapes, bold colors, luxurious, elegant, decorative, symmetrical, ornate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, modernist, minimalist"
    },
    {
        "name": "Art Deco 2",
        "prompt": "Art Deco, {prompt}, sleek, geometric forms, art deco style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Art Nouveau",
        "prompt": "art nouveau style, {prompt}, elegant, decorative, curvilinear forms, nature-inspired, ornate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, modernist, minimalist"
    },
    {
        "name": "Art Nouveau 2",
        "prompt": "Art Nouveau art of {prompt}, sleek, organic forms, long, sinuous, art nouveau style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, industrial, mechanical"
    },
    {
        "name": "Astral Aura",
        "prompt": "Astral Aura, {prompt}, astral, colorful aura, vibrant energy",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Avant-garde",
        "prompt": "Avant-garde, {prompt}, unusual, experimental, avant-garde art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Baroque",
        "prompt": "Baroque, {prompt}, dramatic, exuberant, grandeur, baroque art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Bauhaus-Style Poster",
        "prompt": "Bauhaus-Style Poster, {prompt}, simple geometric shapes, clean lines, primary colors, Bauhaus-Style Poster",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Biomechanical",
        "prompt": "biomechanical style, {prompt}, blend of organic and mechanical elements, futuristic, cybernetic, detailed, intricate",
        "negative_prompt": "natural, rustic, primitive, organic, simplistic"
    },
    {
        "name": "Biomechanical Cyberpunk",
        "prompt": "biomechanical cyberpunk, {prompt}, cybernetics, human-machine fusion, dystopian, organic meets artificial, dark, intricate, highly detailed",
        "negative_prompt": "natural, colorful, deformed, sketch, low contrast, watercolor"
    },
    {
        "name": "Blueprint Schematic Drawing",
        "prompt": "Blueprint Schematic Drawing of {prompt}, technical drawing, blueprint, schematic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Bubble Bobble Game",
        "prompt": "Bubble Bobble style, {prompt}, 8-bit, cute, pixelated, fantasy, vibrant, reminiscent of Bubble Bobble game",
        "negative_prompt": "realistic, modern, photorealistic, violent, horror"
    },
    {
        "name": "Caricature",
        "prompt": "Caricature of {prompt}, exaggerated, comical, caricature",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realistic"
    },
    {
        "name": "Cinematic Film",
        "prompt": "cinematic film still of {prompt}, shallow depth of field, vignette, highly detailed, high budget, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy",
        "negative_prompt": "anime, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured"
    },
    {
        "name": "Cinematic Photograph",
        "prompt": "UHD, 4k, ultra detailed, cinematic, a photograph of {prompt}, epic, beautiful lighting, inpsiring",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realistic"
    },
    {
        "name": "Classicism Art",
        "prompt": "Classicism Art, {prompt}, inspired by Roman and Greek culture, clarity, harmonious, classicism art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Collage",
        "prompt": "Collage style, {prompt}, Mixed media, layered, textural, detailed, artistic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "Commercial Illustration 1920s",
        "prompt": "1920s commercial illustration of {prompt}, magazine cover illustration from the 1920's, exaggerated realism, a hint of caricature",
        "negative_prompt": "monochromatic, ugly, deformed, noisy, blurry, low contrast, photo, photograph, realistic, low res"
    },
    {
        "name": "Comic Book 2",
        "prompt": "comic book art of {prompt}, comic art, graphic novel illustration",
        "negative_prompt": "photograph, deformed, glitch, noisy, realistic, stock photo"
    },
    {
        "name": "Constructivism 1",
        "prompt": "constructivist style, {prompt}, geometric shapes, bold colors, dynamic composition, propaganda art style",
        "negative_prompt": "realistic, photorealistic, low contrast, plain, simple, abstract expressionism"
    },
    {
        "name": "Constructivism 2",
        "prompt": "Constructivism Art of {prompt}, minimalistic, geometric forms, flat, 2D, constructivism art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Craft Clay",
        "prompt": "play-doh style sculpture of {prompt}, sculpture, clay art, centered composition, Claymation",
        "negative_prompt": "sloppy, messy, grainy, highly detailed, ultra textured, photo"
    },
        {
        "name": "Cubism 1",
        "prompt": "Cubist artwork of {prompt}, Geometric shapes, abstract, innovative, revolutionary",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "Cubism 2",
        "prompt": "Cubism Art of {prompt}, flat geometric forms, 2D, limited color palette, cubism art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Cybernetic",
        "prompt": "cybernetic style, {prompt}, futuristic, technological, cybernetic enhancements, robotics, artificial intelligence themes",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, historical, medieval"
    },
    {
        "name": "Cybernetic Robot",
        "prompt": "cybernetic robot {prompt}, android, AI, machine, metal, wires, tech, futuristic, highly detailed",
        "negative_prompt": "organic, natural, human, sketch, watercolor, low contrast"
    },
    {
        "name": "Cyberpunk Cityscape",
        "prompt": "cyberpunk cityscape, {prompt}, neon lights, dark alleys, skyscrapers, futuristic, vibrant colors, high contrast, highly detailed",
        "negative_prompt": "natural, rural, deformed, low contrast, black and white, sketch, watercolor"
    },
    {
        "name": "Cyberpunk",
        "prompt": "cyberpunk style, {prompt}, neon, dystopian, futuristic, digital, vibrant, detailed, high contrast, reminiscent of cyberpunk genre",
        "negative_prompt": "historical, natural, rustic, low detailed"
    },
    {
        "name": "DMT Art Style",
        "prompt": "DMT Art Style of {prompt}, bright colors, surreal visuals, swirling patterns, DMT art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Digital Art",
        "prompt": "concept art of {prompt}, digital artwork, illustrative, painterly, matte painting, highly detailed",
        "negative_prompt": "photo, photorealistic, realism, ugly"
    },
    {
        "name": "Disco",
        "prompt": "Disco-themed, {prompt}, Vibrant, groovy, retro 70s style, shiny disco balls, neon lights, dance floor, highly detailed",
        "negative_prompt": "minimalist, rustic, monochrome, contemporary, simplistic"
    },
    {
        "name": "Double Exposure",
        "prompt": "Double Exposure photography, {prompt}, double image ghost effect, image combination, double exposure style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Dreamscape",
        "prompt": "Dreamscape, {prompt}, Surreal, ethereal, dreamy, mysterious, fantasy, highly detailed",
        "negative_prompt": "realistic, concrete, ordinary, mundane"
    },
    {
        "name": "Dripping Paint Splatter Art",
        "prompt": "Dripping Paint Splatter Art, {prompt}, dramatic, paint drips, splatters, dripping paint",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Dystopian",
        "prompt": "Dystopian style, {prompt}, Bleak, post-apocalyptic, somber, dramatic, highly detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, cheerful, optimistic, vibrant, colorful"
    },
    {
        "name": "Enhance",
        "prompt": "breathtaking, {prompt}, award-winning, professional, highly detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, distorted, grainy"
    },
        {
        "name": "Expressionism 1",
        "prompt": "expressionist, {prompt}, raw, emotional, dynamic, distortion for emotional effect, vibrant, use of unusual colors, detailed",
        "negative_prompt": "realism, symmetry, quiet, calm, photo"
    },
    {
        "name": "Expressionism 2",
        "prompt": "Expressionism Art Style, an expressionist painting of {prompt}, visible brush strokes, contrast, emotional, exaggerated forms, expressionism art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realistic, photograph, photo"
    },
    {
        "name": "Fairy Tale",
        "prompt": "Fairy tale, {prompt}, Magical, fantastical, enchanting, storybook style, highly detailed",
        "negative_prompt": "realistic, modern, ordinary, mundane"
    },
    {
        "name": "Fantasy Art",
        "prompt": "ethereal fantasy concept art of {prompt}, magnificent, celestial, ethereal, painterly, epic, majestic, magical, fantasy art, cover art, dreamy",
        "negative_prompt": "photographic, realistic, realism, 35mm film, dslr, cropped, frame, text, deformed, glitch, noise, noisy, off-center, deformed, cross-eyed, closed eyes, bad anatomy, ugly, disfigured, sloppy, duplicate, mutated, black and white"
    },
    {
        "name": "Fighting Game",
        "prompt": "Fighting game style, {prompt}, Dynamic, vibrant, action-packed, detailed character design, reminiscent of fighting video games",
        "negative_prompt": "peaceful, calm, minimalist, photorealistic"
    },
    {
        "name": "Film Noir 2",
        "prompt": "Film noir style, {prompt}, Monochrome, high contrast, dramatic shadows, 1940s style, mysterious, cinematic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, vibrant, colorful"
    },
    {
        "name": "Flat 2D Art",
        "prompt": "Flat 2D Art of {prompt}, simple flat color, 2-dimensional, Flat 2D Art Style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, 3D, photo, realistic"
    },
    {
        "name": "Flat Papercut",
        "prompt": "Flat papercut style, papercut art of {prompt}, Silhouette, clean cuts, paper, sharp edges, minimalist, color block",
        "negative_prompt": "3D, high detail, noise, grainy, blurry, painting, drawing, photo, disfigured"
    },
    {
        "name": "Food Photography",
        "prompt": "Food photography style, {prompt}, Appetizing, professional, culinary, high-resolution, commercial, highly detailed",
        "negative_prompt": "unappetizing, sloppy, unprofessional, noisy, blurry"
    },
    {
        "name": "Futuristic",
        "prompt": "futuristic style, {prompt}, sleek, modern, ultramodern, high tech, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, vintage, antique"
    },
    {
        "name": "Futuristic Sci-Fi",
        "prompt": "sci-fi style, {prompt}, futuristic, technological, space themes, advanced civilizations",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, historical, medieval"
    },
    {
        "name": "GTA",
        "prompt": "GTA style art of {prompt}, satirical, exaggerated, GTA art style, vibrant colors, iconic characters, action-packed",
        "negative_prompt": "realistic, black and white, low contrast, impressionist, cubist, noisy, blurry, deformed"
    },
    {
        "name": "Glamour",
        "prompt": "glamorous photo of {prompt}, high fashion, luxurious, extravagant, stylish, sensual, opulent, elegance, stunning beauty, professional, high contrast, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, distorted, grainy, sketch, low contrast, dull, plain, modest"
    },
    {
        "name": "Googie Art Style",
        "prompt": "Googie Art Style, {prompt}, dynamic, dramatic, 1950's futurism, bold boomerang angles, Googie art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Gothic",
        "prompt": "Gothic style, {prompt}, Dark, mysterious, haunting, dramatic, ornate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, cheerful, optimistic"
    },
    {
        "name": "Graffiti Art 1",
        "prompt": "Graffiti art of {prompt}, Street art, vibrant, urban, detailed, tag, mural",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "Graffiti Art 2",
        "prompt": "Graffiti art of {prompt}, dynamic, dramatic, vibrant colors, bold lines, graffiti art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Grunge",
        "prompt": "Grunge style, {prompt}, Textured, distressed, vintage, edgy, punk rock vibe, dirty, noisy",
        "negative_prompt": "smooth, clean, minimalist, sleek, modern, photorealistic"
    },
    {
        "name": "HDR",
        "prompt": "HDR photo of {prompt}, High dynamic range, vivid, rich details, clear shadows and highlights, realistic, intense, enhanced contrast, highly detailed",
        "negative_prompt": "flat, low contrast, oversaturated, underexposed, overexposed, blurred, noisy"
    },
    {
        "name": "Harlem Renaissance Art",
        "prompt": "Harlem Renaissance Art Style, {prompt}, dynamic, dramatic, 1920s African American culture, Harlem Renaissance art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "High Fashion",
        "prompt": "High Fashion, {prompt}, dynamic, dramatic, haute couture, elegant, ornate clothing, High Fashion",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Horror",
        "prompt": "Horror-themed, {prompt}, Eerie, unsettling, dark, spooky, suspenseful, grim, highly detailed",
        "negative_prompt": "cheerful, bright, vibrant, light-hearted, cute"
    },
    {
        "name": "Hyperrealism",
        "prompt": "Hyperrealistic art of {prompt}, Extremely high-resolution details, photographic, realism pushed to extreme, fine texture, incredibly lifelike",
        "negative_prompt": "simplified, abstract, unrealistic, impressionistic, low resolution"
    },
    {
        "name": "Idyllic",
        "prompt": "Idyllic, {prompt}, peaceful, happy, pleasant, happy, harmonious, picturesque, charming",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Impressionism 1",
        "prompt": "Impressionist painting of {prompt}, loose brushwork, vibrant color, light and shadow play, captures feeling over form",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "Impressionism 2",
        "prompt": "Impressionism art of {prompt}, painterly, small brushstrokes, visible brushstrokes, impressionistic style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Ink Dripping Drawing",
        "prompt": "Ink Dripping Drawing of {prompt}, ink drawing, ink splash, ink wash, dripping ink",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, colorful, vibrant"
    },
    {
        "name": "Isometric Style",
        "prompt": "isometric style, {prompt}, vibrant, beautiful, crisp, detailed, ultra detailed, intricate, isometric style",
        "negative_prompt": "deformed, mutated, ugly, disfigured, blur, blurry, noise, noisy, realistic, photographic"
    },
    {
        "name": "Japanese Ink Drawing",
        "prompt": "Japanese Style Ink Drawing of {prompt}, ink drawing, inkwash, Japanese Style Ink Drawing",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, colorful, vibrant"
    },
    {
        "name": "Kawaii",
        "prompt": "kawaii style, {prompt}, cute, adorable, brightly colored, cheerful, anime influence, highly detailed",
        "negative_prompt": "dark, scary, realistic, monochrome, abstract"
    },
    {
        "name": "Kirigami",
        "prompt": "Kirigami representation of {prompt}, 3D, paper folding, paper cutting, Japanese, intricate, symmetrical, precision, clean lines",
        "negative_prompt": "painting, drawing, 2D, noisy, blurry, deformed"
    },
    {
        "name": "Knolling Photography",
        "prompt": "Knolling Photography, {prompt}, flat lay photography, object arrangment, knolling photography",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Legend of Zelda",
        "prompt": "Legend of Zelda style art of {prompt}, Vibrant, fantasy, detailed, epic, heroic, reminiscent of The Legend of Zelda series",
        "negative_prompt": "sci-fi, modern, realistic, horror"
    },
    {
        "name": "Light Cheery Atmosphere",
        "prompt": "Light Cheery Atmosphere, {prompt}, happy, joyful, cheerful, carefree, gleeful, lighthearted, pleasant atmosphere",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, monochromatic, dark, moody"
    },
    {
        "name": "Long Exposure",
        "prompt": "Long exposure photo of {prompt}, Blurred motion, streaks of light, surreal, dreamy, ghosting effect, highly detailed",
        "negative_prompt": "static, noisy, deformed, shaky, abrupt, flat, low contrast"
    },
    {
        "name": "Lovecraftian Horror",
        "prompt": "lovecraftian horror, {prompt}, eldritch, cosmic horror, unknown, mysterious, surreal, highly detailed",
        "negative_prompt": "light-hearted, mundane, familiar, simplistic, realistic"
    },
    {
        "name": "Lowpoly",
        "prompt": "low-poly style, {prompt}, low-poly game art, polygon mesh, jagged, blocky, wireframe edges, centered composition",
        "negative_prompt": "noisy, sloppy, messy, grainy, highly detailed, ultra textured, photo"
    },
    {
        "name": "Luxurious Elegance",
        "prompt": "Luxurious Elegance, {prompt}, extravagant, ornate, designer, opulent, picturesque, lavish",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Macabre",
        "prompt": "macabre style, {prompt}, dark, gothic, grim, haunting, highly detailed",
        "negative_prompt": "bright, cheerful, light-hearted, cartoonish, cute"
    },
    {
        "name": "Macro Photography",
        "prompt": "Macro Photography, macro photograph of {prompt}, close-up, macro 100mm, macro photography",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Mandala Art",
        "prompt": "Mandala style art of {prompt}, complex, circular design, mandala art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Manga",
        "prompt": "manga style art of {prompt}, vibrant, high-energy, detailed, iconic, Japanese comic style, manga",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, Western comic style"
    },
    {
        "name": "Medievalism",
        "prompt": "Medievalism, medival art of {prompt}, inspired by The Middle Ages, medieval art, elaborate patterns and decoration, Medievalism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Metropolis",
        "prompt": "metropolis-themed, {prompt}, urban, cityscape, skyscrapers, modern, futuristic, highly detailed",
        "negative_prompt": "rural, natural, rustic, historical, simple"
    },
    {
        "name": "Minecraft",
        "prompt": "Minecraft style art of {prompt}, Blocky, pixelated, vibrant colors, recognizable characters and objects, game assets, Minecraft style",
        "negative_prompt": "smooth, realistic, detailed, photorealistic, noise, blurry, deformed"
    },
    {
        "name": "Minimalism 1",
        "prompt": "Minimalist, {prompt}, Simple, clean, uncluttered, modern, elegant",
        "negative_prompt": "ornate, complicated, highly detailed, cluttered, disordered, messy, noisy"
    },
    {
        "name": "Minimalism 2",
        "prompt": "Minimalism art of {prompt}, abstract, simple geometric shapes, hard edges, sleek contours, Minimalism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Monochrome",
        "prompt": "Monochrome, {prompt}, contrast, tone, texture, detailed, Monochromatic",
        "negative_prompt": "colorful, vibrant, noisy, blurry, deformed"
    },
    {
        "name": "Nautical",
        "prompt": "Nautical-themed, {prompt}, Sea, ocean, ships, maritime, beach, marine life, highly detailed",
        "negative_prompt": "landlocked, desert, mountains, urban, rustic"
    },
    {
        "name": "Neo-Baroque",
        "prompt": "Neo-Baroque, {prompt}, ornate and elaborate, dynamic, Neo-Baroque",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Neo-Byzantine",
        "prompt": "Neo-Byzantine, {prompt}, grand decorative religious style, Orthodox Christian inspired, Neo-Byzantine",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Neo-Futurism",
        "prompt": "Neo-Futurism, {prompt}, high-tech, curves, spirals, flowing lines, idealistic future, Neo-Futurism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Neo-Impressionism",
        "prompt": "Neo-Impressionism, {prompt}, tiny dabs of color, Pointillism, painterly, Neo-Impressionism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photograph, realistic"
    },
    {
        "name": "Neo-Rococo",
        "prompt": "Neo-Rococo, {prompt}, curved forms, naturalistic ornamentation, elaborate, decorative, gaudy, Neo-Rococo",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Neoclassicism",
        "prompt": "Neoclassicism, {prompt}, ancient Rome and Greece inspired, idealic, sober colors, Neoclassicism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Neon Noir",
        "prompt": "Neon noir, {prompt}, Cyberpunk, dark, rainy streets, neon signs, high contrast, low light, vibrant, highly detailed",
        "negative_prompt": "bright, sunny, daytime, low contrast, black and white, sketch, watercolor"
    },
    {
        "name": "Origami",
        "prompt": "origami style, {prompt}, paper art, pleated paper, folded, origami art, pleats, cut and fold, centered composition",
        "negative_prompt": "noisy, sloppy, messy, grainy, highly detailed, ultra textured, photo"
    },
    {
        "name": "Ornate and Intricate",
        "prompt": "Ornate and Intricate, {prompt}, decorative, highly detailed, elaborate, ornate, intricate",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Paper Mache",
        "prompt": "Paper mache representation of {prompt}, 3D, sculptural, textured, handmade, vibrant, fun",
        "negative_prompt": "2D, flat, photo, sketch, digital art, deformed, noisy, blurry"
    },
    {
        "name": "Paper Quilling",
        "prompt": "Paper quilling art of {prompt}, Intricate, delicate, curling, rolling, shaping, coiling, loops, 3D, dimensional, ornamental",
        "negative_prompt": "photo, painting, drawing, 2D, flat, deformed, noisy, blurry"
    },
    {
        "name": "Papercut Collage",
        "prompt": "Papercut collage of {prompt}, Mixed media, textured paper, overlapping, asymmetrical, abstract, vibrant",
        "negative_prompt": "photo, 3D, realistic, drawing, painting, high detail, disfigured"
    },
    {
        "name": "Papercut Shadow Box",
        "prompt": "3D papercut shadow box of {prompt}, Layered, dimensional, depth, silhouette, shadow, papercut, handmade, high contrast",
        "negative_prompt": "painting, drawing, photo, 2D, flat, high detail, blurry, noisy, disfigured"
    },
    {
        "name": "Pencil Sketch",
        "prompt": "Pencil Sketch Drawing of {prompt}, black and white drawing, pencil sketch, graphite drawing",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Pointillism",
        "prompt": "Pointillism style painting of {prompt}, Composed entirely of small distinct dots of color, vibrant, highly detailed, pointillism",
        "negative_prompt": "line drawing, smooth shading, large color fields, simplistic"
    },
    {
        "name": "Pokémon",
        "prompt": "Pokémon style art of {prompt}, Vibrant, cute, anime, fantasy, reminiscent of Pokémon series",
        "negative_prompt": "realistic, modern, horror, dystopian, violent"
    },
    {
        "name": "Pop Art 1",
        "prompt": "Pop Art style, art of {prompt}, Bright colors, bold outlines, popular culture themes, ironic or kitsch",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, minimalist"
    },
    {
        "name": "Pop Art 2",
        "prompt": "Pop Art, art of {prompt}, vivid colors, flat color, 2D, strong lines, Pop Art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photo, realistic"
    },
    {
        "name": "Psychedelic",
        "prompt": "Psychedelic style, {prompt}, Vibrant colors, swirling patterns, abstract forms, surreal, trippy",
        "negative_prompt": "monochrome, black and white, low contrast, realistic, photorealistic, plain, simple"
    },
    {
        "name": "RPG Fantasy",
        "prompt": "Role-playing game (RPG) style fantasy, {prompt}, Detailed, vibrant, immersive, reminiscent of fantasy RPG games",
        "negative_prompt": "sci-fi, modern, urban, futuristic, low detailed"
    },
    {
        "name": "Real Estate Photography",
        "prompt": "Real estate photography style, {prompt}, Professional, inviting, well-lit, high-resolution, property-focused, commercial, highly detailed",
        "negative_prompt": "dark, blurry, unappealing, noisy, unprofessional"
    },
    {
        "name": "Renaissance",
        "prompt": "Renaissance style, {prompt}, Realistic, perspective, light and shadow, religious or mythological themes, highly detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, modernist, minimalist, abstract"
    },
    {
        "name": "Retro Arcade",
        "prompt": "Retro arcade style, {prompt}, 8-bit, pixelated, vibrant, classic video game, old school gaming, reminiscent of 80s and 90s arcade games",
        "negative_prompt": "modern, ultra-high resolution, photorealistic, 3D"
    },
    {
        "name": "Retro Game",
        "prompt": "Retro game art of {prompt}, 16-bit, vibrant colors, pixelated, nostalgic, charming, fun",
        "negative_prompt": "realistic, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "Retro Cyberpunk",
        "prompt": "retro cyberpunk, {prompt}, 1980s inspired, synthwave, neon, vibrant, detailed, retro futurism",
        "negative_prompt": "modern, desaturated, black and white, realism, low contrast"
    },
    {
        "name": "Retro Futurism",
        "prompt": "retro-futuristism, {prompt}, vintage sci-fi, 1950s and 1960s style, atomic age, vibrant, highly detailed, retro futurism",
        "negative_prompt": "contemporary, realistic, rustic, primitive"
    },
    {
        "name": "Rococo",
        "prompt": "Rococo, {prompt}, flamboyant, pastel colors, curved lines, elaborate detail, Rococo",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Silhouette",
        "prompt": "Silhouette style, {prompt}, High contrast, minimalistic, black and white, stark, dramatic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, color, realism, photorealistic"
    },
    {
        "name": "Sketchup",
        "prompt": "Sketchup, {prompt}, CAD, professional design, Sketchup",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photo, photograph"
    },
    {
        "name": "Space",
        "prompt": "Space-themed, {prompt}, Cosmic, celestial, stars, galaxies, nebulas, planets, science fiction, highly detailed",
        "negative_prompt": "earthly, mundane, ground-based, realism"
    },
    {
        "name": "Stacked Papercut",
        "prompt": "Stacked papercut art of {prompt}, 3D, layered, dimensional, depth, precision cut, stacked layers, papercut, high contrast",
        "negative_prompt": "2D, flat, noisy, blurry, painting, drawing, photo, deformed"
    },
    {
        "name": "Stained Glass",
        "prompt": "Stained glass style, {prompt}, Vibrant, beautiful, translucent, intricate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "Steampunk 1",
        "prompt": "Steampunk style, {prompt}, antique, mechanical, brass and copper tones, gears, intricate, detailed",
        "negative_prompt": "deformed, glitch, noisy, low contrast, anime, photorealistic"
    },
    {
        "name": "Steampunk 2",
        "prompt": "Steampunk, {prompt}, retrofuturistic science fantasy, steam-powered tech, vintage industry, gears, neo-victorian, steampunk",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Strategy Game",
        "prompt": "Strategy game style, {prompt}, Overhead view, detailed map, units, reminiscent of real-time strategy video games",
        "negative_prompt": "first-person view, modern, photorealistic"
    },
    {
        "name": "Street Fighter",
        "prompt": "Street Fighter style 2D art of {prompt}, Vibrant, dynamic, arcade, 2D fighting game, highly detailed, reminiscent of Street Fighter series",
        "negative_prompt": "3D, realistic, modern, photorealistic, turn-based strategy"
    },
    {
        "name": "Super Mario",
        "prompt": "Super Mario style art of {prompt}, Vibrant, cute, cartoony, fantasy, playful, reminiscent of Super Mario series",
        "negative_prompt": "realistic, modern, horror, dystopian, violent"
    },
    {
        "name": "Suprematism",
        "prompt": "Suprematism, {prompt}, abstract, limited color palette, geometric forms, Suprematism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realistic"
    },
    {
        "name": "Surrealism 1",
        "prompt": "Surrealist art {prompt}, dreamlike, mysterious, provocative, symbolic, intricate, detailed",
        "negative_prompt": "anime, photorealistic, realistic, deformed, glitch, noisy, low contrast"
    },
    {
        "name": "Surrealism 2",
        "prompt": "Surrealism, {prompt}, expressive, dramatic, organic lines and forms, dreamlike, mysterious, Surrealism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realistic"
    },
    {
        "name": "Techwear Fashion",
        "prompt": "Techwear fashion, {prompt}, Futuristic, cyberpunk, urban, tactical, sleek, dark, highly detailed",
        "negative_prompt": "vintage, rural, colorful, low contrast, realism, sketch, watercolor"
    },
    {
        "name": "Terragen",
        "prompt": "Terragen, {prompt}, beautiful massive landscape, epic scenery, Terragen",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Texture",
        "prompt": "texture asset, seamless texture of {prompt}, close-up, texture detail, tileable texture",
        "negative_prompt": "ugly, deformed, noisy, blurry"
    },
    {
        "name": "Thick Layered Papercut",
        "prompt": "Thick layered papercut art of {prompt}, Deep 3D, volumetric, dimensional, depth, thick paper, high stack, heavy texture, tangible layers",
        "negative_prompt": "2D, flat, thin paper, low stack, smooth texture, painting, drawing, photo, deformed"
    },
    {
        "name": "Tilt-Shift Photo",
        "prompt": "Tilt-shift photo of {prompt}, selective focus, miniature effect, blurred background, highly detailed, vibrant, perspective control",
        "negative_prompt": "blurry, noisy, deformed, flat, low contrast, unrealistic, oversaturated, underexposed"
    },
    {
        "name": "Tranquil Relaxing Atmosphere",
        "prompt": "Tranquil Relaxing Atmosphere, {prompt}, calming style, soothing colors, peaceful, idealic, Tranquil Relaxing Atmosphere",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, oversaturated"
    },
    {
        "name": "Tribal",
        "prompt": "Tribal style, {prompt}, Indigenous, ethnic, traditional patterns, bold, natural colors, highly detailed",
        "negative_prompt": "modern, futuristic, minimalist, pastel"
    },
    {
        "name": "Typography",
        "prompt": "Typographic art of {prompt}, Stylized, intricate, detailed, artistic, text-based",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "Vaporwave",
        "prompt": "vaporwave style, {prompt}, retro aesthetic, cyberpunk, vibrant, neon colors, vintage 80s and 90s style, highly detailed",
        "negative_prompt": "monochrome, muted colors, realism, rustic, minimalist, dark"
    },
    {
        "name": "Vibrant Rim Light",
        "prompt": "Vibrant Rim Light, {prompt}, back lighting, beautiful lighting, colored rim light, high contrast",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Watercolor 2",
        "prompt": "Watercolor style painting, {prompt}, visible paper texture, colorwash, watercolor art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photo, realistic"
    },
    {
        "name": "Whimsical and Playful",
        "prompt": "Whimsical and Playful, {prompt}, imaginative, fantastical, bight colors, stylized, happy, Whimsical and Playful",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, drab, boring, moody"
    },
    {
        "name": "Wild West",
        "prompt": "wild west style, {prompt}, the old west, historical, rustic, the wild west",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, drab, boring, moody"
    },
    {
        "name": "Zentangle",
        "prompt": "Zentangle, {prompt}, Intricate, abstract, monochrome, patterns, meditative, highly detailed",
        "negative_prompt": "colorful, representative, simplistic, large fields of color"
    },
    {
        "name": "ads-automotive",
        "prompt": "automotive advertisement style, {prompt}, sleek, dynamic, professional, commercial, vehicle-focused, high-resolution, highly detailed",
        "negative_prompt": "noisy, blurry, unattractive, sloppy, unprofessional"
    },
    {
        "name": "ads-corporate",
        "prompt": "corporate branding style, {prompt}, professional, clean, modern, sleek, minimalist, business-oriented, highly detailed",
        "negative_prompt": "noisy, blurry, grungy, sloppy, cluttered, disorganized"
    },
    {
        "name": "ads-fashion editorial",
        "prompt": "fashion editorial style, {prompt}, high fashion, trendy, stylish, editorial, magazine style, professional, highly detailed",
        "negative_prompt": "outdated, blurry, noisy, unattractive, sloppy"
    },
    {
        "name": "ads-food photography",
        "prompt": "food photography style, {prompt}, appetizing, professional, culinary, high-resolution, commercial, highly detailed",
        "negative_prompt": "unappetizing, sloppy, unprofessional, noisy, blurry"
    },
    {
        "name": "ads-gourmet food photography",
        "prompt": "gourmet food photo of {prompt}, soft natural lighting, macro details, vibrant colors, fresh ingredients, glistening textures, bokeh background, styled plating, wooden tabletop, garnished, tantalizing, editorial quality",
        "negative_prompt": "cartoon, anime, sketch, grayscale, dull, overexposed, cluttered, messy plate, deformed"
    },
    {
        "name": "ads-luxury",
        "prompt": "luxury product style, {prompt}, elegant, sophisticated, high-end, luxurious, professional, highly detailed",
        "negative_prompt": "cheap, noisy, blurry, unattractive, amateurish"
    },
    {
        "name": "ads-real estate",
        "prompt": "real estate photography style, {prompt}, professional, inviting, well-lit, high-resolution, property-focused, commercial, highly detailed",
        "negative_prompt": "dark, blurry, unappealing, noisy, unprofessional"
    },
    {
        "name": "ads-retail",
        "prompt": "retail packaging style, {prompt}, vibrant, enticing, commercial, product-focused, eye-catching, professional, highly detailed",
        "negative_prompt": "noisy, blurry, amateurish, sloppy, unattractive"
    },
    {
        "name": "img2img 3d to photorealisim",
        "prompt": "RAW photo, (high detailed skin:1.2), 8k uhd, dslr, soft lighting, high quality, film grain, Fujifilm XT3",
        "negative_prompt": "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck"
    },
    {
        "name": "Magnetic Ink",
        "prompt": "magnetic ink style of {prompt}, experimental, swirling magnetic fluid patterns, surreal, dark elegance, fine detail",
        "negative_prompt": "realistic, flat, bland, overly bright, photorealistic, sketch, digital"
    },
    {
        "name": "Mythological Mosaic",
        "prompt": "mythological mosaic of {prompt}, intricate tiles, Byzantine influence, divine symbolism, ornamental, richly colored",
        "negative_prompt": "plain, modern, simple, minimalistic, sketchy, blurry, noisy"
    },
    {
        "name": "Nebula Dreams",
        "prompt": "ethereal nebula of {prompt}, colorful gas clouds, cosmic glow, vibrant, surreal, deep space vision",
        "negative_prompt": "earthly, monotone, deformed, low contrast, cartoon, flat design"
    },
    {
        "name": "Oceanic Abstraction",
        "prompt": "abstract oceanic interpretation of {prompt}, fluid motion, blues and greens, wave forms, flowing energy",
        "negative_prompt": "stiff, rigid, geometric, land-themed, urban, black and white"
    },
    {
        "name": "Paper Origami Galaxy",
        "prompt": "galactic origami of {prompt}, folded paper representing space, stars, planets, artistic fusion of origami and cosmos",
        "negative_prompt": "photo, 3D render, realism, low detail, dull, sketchy, natural"
    },
    {
        "name": "Quantum Graffiti",
        "prompt": "quantum graffiti of {prompt}, neon particles, motion trails, vibrant stencils, physics-themed abstract art",
        "negative_prompt": "low energy, static, plain, dull, black and white, traditional"
    },
    {
        "name": "Retro Botanical",
        "prompt": "retro botanical print of {prompt}, vintage flora, 60s style, bold outlines, muted natural palette, textural detail",
        "negative_prompt": "digital look, glitch, synthetic, geometric, sci-fi, horror"
    },
    {
        "name": "Solarpunk Harmony",
        "prompt": "solarpunk vision of {prompt}, hopeful eco-future, warm lighting, greenery-integrated architecture, golden hour, organic tech",
        "negative_prompt": "dystopian, dark, monochrome, industrial, gritty, cyberpunk"
    },
    {
        "name": "Tactile Velvet",
        "prompt": "velvet texture visual of {prompt}, soft, lush, luxurious fabric aesthetic, deep shadows, high fidelity tactile style",
        "negative_prompt": "rough, papery, low texture, flat, blurry, noisy, sketchy"
    },
    {
        "name": "Ultraviolet Minimalism",
        "prompt": "ultraviolet minimalist representation of {prompt}, clean lines, glowing neon, blacklight aesthetics, futuristic restraint",
        "negative_prompt": "ornate, cluttered, dull colors, realism, heavy texture, painterly"
    },
    {
        "name": "Vintage Newsprint",
        "prompt": "vintage newsprint style of {prompt}, monochrome halftone, 1950s newspaper aesthetic, slightly yellowed paper, ink bleed",
        "negative_prompt": "modern print, digital, color photography, glossy, high contrast"
    },
    {
        "name": "Woven Textile Pattern",
        "prompt": "woven textile pattern of {prompt}, thread textures, tapestry style, intricate weave, folk art inspired",
        "negative_prompt": "flat, digital art, noisy, blurry, pixelated, neon colors"
    },
    {
        "name": "Xerox Decay",
        "prompt": "xerox photocopy decay of {prompt}, scanned texture, overexposed shadows, ghosted repetition, lo-fi print artifact",
        "negative_prompt": "high detail, color accurate, realistic, high fidelity, vibrant"
    },
    {
        "name": "Yarn Craft Illustration",
        "prompt": "yarn-crafted illustration of {prompt}, embroidered edges, fiber texture, handcrafted warmth, cozy aesthetic",
        "negative_prompt": "sharp lines, digital smoothness, 3D render, photo-real, cool tone"
    },
    {
        "name": "Zen Minimal Brushwork",
        "prompt": "Zen minimal ink brush style of {prompt}, sumi-e, focused form, intentional space, meditative, spiritual",
        "negative_prompt": "colorful, busy, textured, complex, realistic, noisy"
    },
    {
        "name": "Zero Gravity Fantasy",
        "prompt": "zero gravity dreamscape of {prompt}, floating elements, anti-physics, surreal weightlessness, soft edges, luminous atmosphere",
        "negative_prompt": "grounded, rigid, realistic, photographic, hard shadows, dry texture"
    },
    {
        "name": "Zodiac Ritual Illustration",
        "prompt": "mystical zodiac ritual illustration of {prompt}, celestial symbology, arcane circles, star charts, magical ink lines, parchment paper",
        "negative_prompt": "modern, flat, digital, realism, cartoon, photo, sketch"
    },
    {
        "name": "Zoological Scientific Plate",
        "prompt": "vintage scientific plate of {prompt}, detailed zoological illustration, labeled anatomy, 19th century textbook style",
        "negative_prompt": "photo, modern, stylized, blurry, cartoony, fantasy"
    },
    {
        "name": "Ancient Fresco",
        "prompt": "ancient fresco mural of {prompt}, weathered wall texture, Renaissance or Greco-Roman style, faded pigments, historical ambiance",
        "negative_prompt": "digital, clean, photorealistic, modern, saturated, polished"
    },
    {
        "name": "Bioluminescent Dreamscape",
        "prompt": "bioluminescent dreamscape of {prompt}, glowing flora and fauna, surreal night environment, mystical lighting, soft hues",
        "negative_prompt": "harsh light, realism, flat tones, washed out, gray, noisy"
    },
    {
        "name": "Crystal Core Fantasy",
        "prompt": "crystal core fantasy setting of {prompt}, glowing crystals, refracted light, geode textures, fantasy cavern",
        "negative_prompt": "urban, plain, metallic, untextured, modernist, minimal"
    },
    {
        "name": "Dream Journal Sketch",
        "prompt": "dream journal sketch of {prompt}, hazy lines, half-remembered forms, scribbled notes, surreal and personal",
        "negative_prompt": "sharp lines, high detail, vector art, polished, 3D"
    },
    {
        "name": "Escher Maze",
        "prompt": "Escher-inspired maze of {prompt}, impossible geometry, infinite staircases, optical illusions, paradoxical architecture",
        "negative_prompt": "natural, flowing, organic, realistic, bright, earthy"
    },
    {
        "name": "Floating Ink Surrealism",
        "prompt": "floating ink surrealism of {prompt}, ink suspended mid-air, dreamlike visuals, dripping space, anti-gravity composition",
        "negative_prompt": "concrete, photographic, sketchy, low saturation, earthy"
    },
    {
        "name": "Glass Garden",
        "prompt": "glass garden scene of {prompt}, crystalline plants, translucent flowers, stained-glass reflections, fantasy botany",
        "negative_prompt": "muddy, opaque, textured, wooden, faded, dry"
    },
    {
        "name": "Holographic Prism",
        "prompt": "holographic prism style of {prompt}, iridescent reflections, rainbow interference patterns, tech-futuristic glow",
        "negative_prompt": "flat color, grayscale, vintage, dull, matte"
    },
    {
        "name": "Iridescent Oil Painting",
        "prompt": "iridescent oil painting of {prompt}, shimmering textures, rich pigments, glowing brushstrokes, dynamic lighting",
        "negative_prompt": "matte, flat, pastel, sketch, blurry, noise-heavy"
    },
    {
        "name": "Jellyfish Bloom",
        "prompt": "jellyfish bloom concept of {prompt}, ethereal underwater swarms, bioluminescent trails, oceanic glow, drifting composition",
        "negative_prompt": "dry, sharp, solid, land-based, hot, structured"
    },
    {
        "name": "Kaleidoscope Portal",
        "prompt": "kaleidoscope portal view of {prompt}, fractal symmetry, mirrored shards, shifting colors, geometric chaos",
        "negative_prompt": "flat, monochrome, photorealistic, linear, simple, minimal"
    },
    {
        "name": "Lantern Festival",
        "prompt": "lantern festival depiction of {prompt}, glowing paper lanterns, night celebration, ambient warmth, floating lights",
        "negative_prompt": "daylight, dry, monochrome, indoor, noisy, sharp"
    },
    {
        "name": "Meteorite Sketchbook",
        "prompt": "meteorite sketchbook drawing of {prompt}, cosmic debris, space rock studies, charcoal shading, hand-drawn look",
        "negative_prompt": "clean vector, colorful, 3D, polished, synthetic"
    },
    {
        "name": "Nightlight Plush Scene",
        "prompt": "cozy nightlight scene of {prompt}, plush textures, soft glowing light, dreamy bedtime aesthetic, childlike comfort",
        "negative_prompt": "harsh lighting, sharp shadows, hard materials, realistic"
    },
    {
        "name": "Opalescent Layered Glass",
        "prompt": "opalescent layered glass art of {prompt}, milky translucent hues, layered texture, dreamlike glow, soft focus",
        "negative_prompt": "matte, opaque, dry, flat, solid black and white"
    },
    {
        "name": "Fooocus V2",
        "prompt": "{prompt}, highly detailed, dramatic light, sharp focus, illuminated, cinematic, fine detail, polished, complex, color, pristine, attractive, celestial, symmetry, pretty, striking, extremely, coherent, cute, confident, united, passionate, professional, artistic, ambient, cheerful, intricate, magical, enchanted, magic, stunning, beautiful",
        "negative_prompt": ""
    },
    {
        "name": "Fooocus Sharp",
        "prompt": "cinematic still {prompt}. emotional, harmonious, vignette, 4k epic detailed, shot on kodak, 35mm photo, sharp focus, high budget, cinemascope, moody, epic, gorgeous, film grain, grainy",
        "negative_prompt": "anime, cartoon, graphic, (blur, blurry, bokeh), text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured"
    },
    {
        "name": "Fooocus Masterpiece",
        "prompt": "(masterpiece), (best quality), (ultra-detailed), {prompt}, illustration, disheveled hair, detailed eyes, perfect composition, moist skin, intricate details, earrings, by wlop",
        "negative_prompt": "longbody, lowres, bad anatomy, bad hands, missing fingers, pubic hair,extra digit, fewer digits, cropped, worst quality, low quality"
    },
    {
        "name": "Fooocus Photograph",
        "prompt": "photograph {prompt}, 50mm . cinematic 4k epic detailed 4k epic detailed photograph shot on kodak detailed cinematic hbo dark moody, 35mm photo, grainy, vignette, vintage, Kodachrome, Lomography, stained, highly detailed, found footage",
        "negative_prompt": "Brad Pitt, bokeh, depth of field, blurry, cropped, regular face, saturated, contrast, deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime, text, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck"
    },
    {
        "name": "Fooocus Negative",
        "prompt": "{prompt}",
        "negative_prompt": "deformed, bad anatomy, disfigured, poorly drawn face, mutated, extra limb, ugly, poorly drawn hands, missing limb, floating limbs, disconnected limbs, disconnected head, malformed hands, long neck, mutated hands and fingers, bad hands, missing fingers, cropped, worst quality, low quality, mutation, poorly drawn, huge calf, bad hands, fused hand, missing hand, disappearing arms, disappearing thigh, disappearing calf, disappearing legs, missing fingers, fused fingers, abnormal eye proportion, Abnormal hands, abnormal legs, abnormal feet, abnormal fingers, drawing, painting, crayon, sketch, graphite, impressionist, noisy, blurry, soft, deformed, ugly, anime, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch"
    },
    {
        "name": "3D Model",
        "prompt": "professional 3d model {prompt}. octane render, highly detailed, volumetric, dramatic lighting",
        "negative_prompt": "ugly, deformed, noisy, low poly, blurry, painting"
    },
    {
        "name": "Analog Film",
        "prompt": "analog film photo {prompt}. faded film, desaturated, 35mm photo, grainy, vignette, vintage, Kodachrome, Lomography, stained, highly detailed, found footage",
        "negative_prompt": "painting, drawing, illustration, glitch, deformed, mutated, cross-eyed, ugly, disfigured"
    },
    {
        "name": "Pixel Art",
        "prompt": "pixel-art {prompt}. low-res, blocky, pixel art style, 8-bit graphics",
        "negative_prompt": "sloppy, messy, blurry, noisy, highly detailed, ultra textured, photo, realistic"
    },
    {
        "name": "Texture 2",
        "prompt": "texture {prompt} top down close-up",
        "negative_prompt": "ugly, deformed, noisy, blurry"
    },
    {
        "name": "MRE Cinematic Dynamic",
        "prompt": "epic cinematic shot of dynamic {prompt} in motion. main subject of high budget action movie. raw photo, motion blur. best quality, high resolution",
        "negative_prompt": "static, still, motionless, sluggish. drawing, painting, illustration, rendered. low budget. low quality, low resolution"
    },
    {
        "name": "MRE Spontaneous Picture",
        "prompt": "spontaneous picture of {prompt}, taken by talented amateur. best quality, high resolution. magical moment, natural look. simple but good looking",
        "negative_prompt": "overthinked. low quality, low resolution"
    },
    {
        "name": "MRE Artistic Vision",
        "prompt": "powerful artistic vision of {prompt}. breathtaking masterpiece made by great artist. best quality, high resolution",
        "negative_prompt": "insignificant, flawed, made by bad artist. low quality, low resolution"
    },
    {
        "name": "MRE Dark Dream",
        "prompt": "dark and unsettling dream showing {prompt}. best quality, high resolution. created by genius but depressed mad artist. grim beauty",
        "negative_prompt": "naive, cheerful. comfortable, casual, boring, cliche. low quality, low resolution"
    },
    {
        "name": "MRE Gloomy Art",
        "prompt": "astonishing gloomy art made mainly of shadows and lighting, forming {prompt}. masterful usage of lighting, shadows and chiaroscuro. made by black-hearted artist, drawing from darkness. best quality, high resolution",
        "negative_prompt": "low quality, low resolution"
    },
    {
        "name": "MRE Bad Dream",
        "prompt": "picture from really bad dream about terrifying {prompt}, true horror. bone-chilling vision. mad world that shouldn't exist. best quality, high resolution",
        "negative_prompt": "nice dream, pleasant experience. low quality, low resolution"
    },
    {
        "name": "MRE Underground",
        "prompt": "uncanny caliginous vision of {prompt}, created by remarkable underground artist. best quality, high resolution. raw and brutal art, careless but impressive style. inspired by darkness and chaos",
        "negative_prompt": "photography, mainstream, civilized. low quality, low resolution"
    },
    {
        "name": "MRE Surreal Painting",
        "prompt": "surreal painting representing strange vision of {prompt}. harmonious madness, synergy with chance. unique artstyle, mindbending art, magical surrealism. best quality, high resolution",
        "negative_prompt": "photography, illustration, drawing. realistic, possible. logical, sane. low quality, low resolution"
    },
    {
        "name": "MRE Dynamic Illustration",
        "prompt": "insanely dynamic illustration of {prompt}. best quality, high resolution. crazy artstyle, careless brushstrokes, emotional and fun",
        "negative_prompt": "photography, realistic. static, still, slow, boring. low quality, low resolution"
    },
    {
        "name": "MRE Undead Art",
        "prompt": "long forgotten art created by undead artist illustrating {prompt}, tribute to the death and decay. miserable art of the damned. wretched and decaying world. best quality, high resolution",
        "negative_prompt": "alive, playful, living. low quality, low resolution"
    },
    {
        "name": "MRE Elemental Art",
        "prompt": "art illustrating insane amounts of raging elemental energy turning into {prompt}, avatar of elements. magical surrealism, wizardry. best quality, high resolution",
        "negative_prompt": "photography, realistic, real. low quality, low resolution"
    },
    {
        "name": "MRE Space Art",
        "prompt": "winner of inter-galactic art contest illustrating {prompt}, symbol of the interstellar singularity. best quality, high resolution. artstyle previously unseen in the whole galaxy",
        "negative_prompt": "created by human race, low quality, low resolution"
    },
    {
        "name": "MRE Ancient Illustration",
        "prompt": "sublime ancient illustration of {prompt}, predating human civilization. crude and simple, but also surprisingly beautiful artwork, made by genius primeval artist. best quality, high resolution",
        "negative_prompt": "low quality, low resolution"
    },
    {
        "name": "MRE Brave Art",
        "prompt": "brave, shocking, and brutally true art showing {prompt}. inspired by courage and unlimited creativity. truth found in chaos. best quality, high resolution",
        "negative_prompt": "low quality, low resolution"
    },
    {
        "name": "MRE Heroic Fantasy",
        "prompt": "heroic fantasy painting of {prompt}, in the dangerous fantasy world. airbrush over oil on canvas. best quality, high resolution",
        "negative_prompt": "low quality, low resolution"
    },
    {
        "name": "MRE Dark Cyberpunk",
        "prompt": "dark cyberpunk illustration of brutal {prompt} in a world without hope, ruled by ruthless criminal corporations. best quality, high resolution",
        "negative_prompt": "low quality, low resolution"
    },
    {
        "name": "MRE Lyrical Geometry",
        "prompt": "geometric and lyrical abstraction painting presenting {prompt}. oil on metal. best quality, high resolution",
        "negative_prompt": "photography, realistic, drawing, rendered. low quality, low resolution"
    },
    {
        "name": "MRE Sumi E Symbolic",
        "prompt": "big long brushstrokes of deep black sumi-e turning into symbolic painting of {prompt}. master level raw art. best quality, high resolution",
        "negative_prompt": "photography, rendered. low quality, low resolution"
    },
    {
        "name": "MRE Sumi E Detailed",
        "prompt": "highly detailed black sumi-e painting of {prompt}. in-depth study of perfection, created by a master. best quality, high resolution",
        "negative_prompt": "low quality, low resolution"
    },
    {
        "name": "MRE Manga",
        "prompt": "manga artwork presenting {prompt}. created by japanese manga artist. highly emotional. best quality, high resolution",
        "negative_prompt": "low quality, low resolution"
    },
    {
        "name": "MRE Anime",
        "prompt": "anime artwork illustrating {prompt}. created by japanese anime studio. highly emotional. best quality, high resolution",
        "negative_prompt": "low quality, low resolution"
    },
    {
        "name": "MRE Comic",
        "prompt": "breathtaking illustration from adult comic book presenting {prompt}. fabulous artwork. best quality, high resolution",
        "negative_prompt": "deformed, ugly, low quality, low resolution"
    },
    {
        "name": "Ads Automotive",
        "prompt": "automotive advertisement style {prompt}. sleek, dynamic, professional, commercial, vehicle-focused, high-resolution, highly detailed",
        "negative_prompt": "noisy, blurry, unattractive, sloppy, unprofessional"
    },
    {
        "name": "Ads Corporate",
        "prompt": "corporate branding style {prompt}. professional, clean, modern, sleek, minimalist, business-oriented, highly detailed",
        "negative_prompt": "noisy, blurry, grungy, sloppy, cluttered, disorganized"
    },
    {
        "name": "Ads Fashion Editorial",
        "prompt": "fashion editorial style {prompt}. high fashion, trendy, stylish, editorial, magazine style, professional, highly detailed",
        "negative_prompt": "outdated, blurry, noisy, unattractive, sloppy"
    },
    {
        "name": "Ads Food Photography",
        "prompt": "food photography style {prompt}. appetizing, professional, culinary, high-resolution, commercial, highly detailed",
        "negative_prompt": "unappetizing, sloppy, unprofessional, noisy, blurry"
    },
    {
        "name": "Ads Gourmet Food Photography",
        "prompt": "gourmet food photo of {prompt}. soft natural lighting, macro details, vibrant colors, fresh ingredients, glistening textures, bokeh background, styled plating, wooden tabletop, garnished, tantalizing, editorial quality",
        "negative_prompt": "cartoon, anime, sketch, grayscale, dull, overexposed, cluttered, messy plate, deformed"
    },
    {
        "name": "Ads Luxury",
        "prompt": "luxury product style {prompt}. elegant, sophisticated, high-end, luxurious, professional, highly detailed",
        "negative_prompt": "cheap, noisy, blurry, unattractive, amateurish"
    },
    {
        "name": "Ads Real Estate",
        "prompt": "real estate photography style {prompt}. professional, inviting, well-lit, high-resolution, property-focused, commercial, highly detailed",
        "negative_prompt": "dark, blurry, unappealing, noisy, unprofessional"
    },
    {
        "name": "Ads Retail",
        "prompt": "retail packaging style {prompt}. vibrant, enticing, commercial, product-focused, eye-catching, professional, highly detailed",
        "negative_prompt": "noisy, blurry, amateurish, sloppy, unattractive"
    },
    {
        "name": "Artstyle Abstract",
        "prompt": "abstract style {prompt}. non-representational, colors and shapes, expression of feelings, imaginative, highly detailed",
        "negative_prompt": "realistic, photographic, figurative, concrete"
    },
    {
        "name": "Artstyle Abstract Expressionism",
        "prompt": "abstract expressionist painting {prompt}. energetic brushwork, bold colors, abstract forms, expressive, emotional",
        "negative_prompt": "realistic, photorealistic, low contrast, plain, simple, monochrome"
    },
    {
        "name": "Artstyle Art Deco",
        "prompt": "art deco style {prompt}. geometric shapes, bold colors, luxurious, elegant, decorative, symmetrical, ornate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, modernist, minimalist"
    },
    {
        "name": "Artstyle Art Nouveau",
        "prompt": "art nouveau style {prompt}. elegant, decorative, curvilinear forms, nature-inspired, ornate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, modernist, minimalist"
    },
    {
        "name": "Artstyle Constructivist",
        "prompt": "constructivist style {prompt}. geometric shapes, bold colors, dynamic composition, propaganda art style",
        "negative_prompt": "realistic, photorealistic, low contrast, plain, simple, abstract expressionism"
    },
    {
        "name": "Artstyle Cubist",
        "prompt": "cubist artwork {prompt}. geometric shapes, abstract, innovative, revolutionary",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "Artstyle Expressionist",
        "prompt": "expressionist {prompt}. raw, emotional, dynamic, distortion for emotional effect, vibrant, use of unusual colors, detailed",
        "negative_prompt": "realism, symmetry, quiet, calm, photo"
    },
    {
        "name": "Artstyle Graffiti",
        "prompt": "graffiti style {prompt}. street art, vibrant, urban, detailed, tag, mural",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "Artstyle Hyperrealism",
        "prompt": "hyperrealistic art {prompt}. extremely high-resolution details, photographic, realism pushed to extreme, fine texture, incredibly lifelike",
        "negative_prompt": "simplified, abstract, unrealistic, impressionistic, low resolution"
    },
    {
        "name": "Artstyle Impressionist",
        "prompt": "impressionist painting {prompt}. loose brushwork, vibrant color, light and shadow play, captures feeling over form",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "Artstyle Pointillism",
        "prompt": "pointillism style {prompt}. composed entirely of small, distinct dots of color, vibrant, highly detailed",
        "negative_prompt": "line drawing, smooth shading, large color fields, simplistic"
    },
    {
        "name": "Artstyle Pop Art",
        "prompt": "pop Art style {prompt}. bright colors, bold outlines, popular culture themes, ironic or kitsch",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, minimalist"
    },
    {
        "name": "Artstyle Psychedelic",
        "prompt": "psychedelic style {prompt}. vibrant colors, swirling patterns, abstract forms, surreal, trippy",
        "negative_prompt": "monochrome, black and white, low contrast, realistic, photorealistic, plain, simple"
    },
    {
        "name": "Artstyle Renaissance",
        "prompt": "renaissance style {prompt}. realistic, perspective, light and shadow, religious or mythological themes, highly detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, modernist, minimalist, abstract"
    },
    {
        "name": "Artstyle Steampunk",
        "prompt": "steampunk style {prompt}. antique, mechanical, brass and copper tones, gears, intricate, detailed",
        "negative_prompt": "deformed, glitch, noisy, low contrast, anime, photorealistic"
    },
    {
        "name": "Artstyle Surrealist",
        "prompt": "surrealist art {prompt}. dreamlike, mysterious, provocative, symbolic, intricate, detailed",
        "negative_prompt": "anime, photorealistic, realistic, deformed, glitch, noisy, low contrast"
    },
    {
        "name": "Artstyle Typography",
        "prompt": "typographic art {prompt}. stylized, intricate, detailed, artistic, text-based",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "Artstyle Watercolor",
        "prompt": "watercolor painting {prompt}. vibrant, beautiful, painterly, detailed, textural, artistic",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "Futuristic Biomechanical",
        "prompt": "biomechanical style {prompt}. blend of organic and mechanical elements, futuristic, cybernetic, detailed, intricate",
        "negative_prompt": "natural, rustic, primitive, organic, simplistic"
    },
    {
        "name": "Futuristic Biomechanical Cyberpunk",
        "prompt": "biomechanical cyberpunk {prompt}. cybernetics, human-machine fusion, dystopian, organic meets artificial, dark, intricate, highly detailed",
        "negative_prompt": "natural, colorful, deformed, sketch, low contrast, watercolor"
    },
    {
        "name": "Futuristic Cybernetic",
        "prompt": "cybernetic style {prompt}. futuristic, technological, cybernetic enhancements, robotics, artificial intelligence themes",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, historical, medieval"
    },
    {
        "name": "Futuristic Cybernetic Robot",
        "prompt": "cybernetic robot {prompt}. android, AI, machine, metal, wires, tech, futuristic, highly detailed",
        "negative_prompt": "organic, natural, human, sketch, watercolor, low contrast"
    },
    {
        "name": "Futuristic Cyberpunk Cityscape",
        "prompt": "cyberpunk cityscape {prompt}. neon lights, dark alleys, skyscrapers, futuristic, vibrant colors, high contrast, highly detailed",
        "negative_prompt": "natural, rural, deformed, low contrast, black and white, sketch, watercolor"
    },
    {
        "name": "Futuristic Futuristic",
        "prompt": "futuristic style {prompt}. sleek, modern, ultramodern, high tech, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, vintage, antique"
    },
    {
        "name": "Futuristic Retro Cyberpunk",
        "prompt": "retro cyberpunk {prompt}. 80's inspired, synthwave, neon, vibrant, detailed, retro futurism",
        "negative_prompt": "modern, desaturated, black and white, realism, low contrast"
    },
    {
        "name": "Futuristic Retro Futurism",
        "prompt": "retro-futuristic {prompt}. vintage sci-fi, 50s and 60s style, atomic age, vibrant, highly detailed",
        "negative_prompt": "contemporary, realistic, rustic, primitive"
    },
    {
        "name": "Futuristic Sci Fi",
        "prompt": "sci-fi style {prompt}. futuristic, technological, alien worlds, space themes, advanced civilizations",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, historical, medieval"
    },
    {
        "name": "Futuristic Vaporwave",
        "prompt": "vaporwave style {prompt}. retro aesthetic, cyberpunk, vibrant, neon colors, vintage 80s and 90s style, highly detailed",
        "negative_prompt": "monochrome, muted colors, realism, rustic, minimalist, dark"
    },
    {
        "name": "Game Bubble Bobble",
        "prompt": "Bubble Bobble style {prompt}. 8-bit, cute, pixelated, fantasy, vibrant, reminiscent of Bubble Bobble game",
        "negative_prompt": "realistic, modern, photorealistic, violent, horror"
    },
    {
        "name": "Game Cyberpunk Game",
        "prompt": "cyberpunk game style {prompt}. neon, dystopian, futuristic, digital, vibrant, detailed, high contrast, reminiscent of cyberpunk genre video games",
        "negative_prompt": "historical, natural, rustic, low detailed"
    },
    {
        "name": "Game Fighting Game",
        "prompt": "fighting game style {prompt}. dynamic, vibrant, action-packed, detailed character design, reminiscent of fighting video games",
        "negative_prompt": "peaceful, calm, minimalist, photorealistic"
    },
    {
        "name": "Game Gta",
        "prompt": "GTA-style artwork {prompt}. satirical, exaggerated, pop art style, vibrant colors, iconic characters, action-packed",
        "negative_prompt": "realistic, black and white, low contrast, impressionist, cubist, noisy, blurry, deformed"
    },
    {
        "name": "Game Mario",
        "prompt": "Super Mario style {prompt}. vibrant, cute, cartoony, fantasy, playful, reminiscent of Super Mario series",
        "negative_prompt": "realistic, modern, horror, dystopian, violent"
    },
    {
        "name": "Game Minecraft",
        "prompt": "Minecraft style {prompt}. blocky, pixelated, vibrant colors, recognizable characters and objects, game assets",
        "negative_prompt": "smooth, realistic, detailed, photorealistic, noise, blurry, deformed"
    },
    {
        "name": "Game Pokemon",
        "prompt": "Pokémon style {prompt}. vibrant, cute, anime, fantasy, reminiscent of Pokémon series",
        "negative_prompt": "realistic, modern, horror, dystopian, violent"
    },
    {
        "name": "Game Retro Arcade",
        "prompt": "retro arcade style {prompt}. 8-bit, pixelated, vibrant, classic video game, old school gaming, reminiscent of 80s and 90s arcade games",
        "negative_prompt": "modern, ultra-high resolution, photorealistic, 3D"
    },
    {
        "name": "Game Rpg Fantasy Game",
        "prompt": "role-playing game (RPG) style fantasy {prompt}. detailed, vibrant, immersive, reminiscent of high fantasy RPG games",
        "negative_prompt": "sci-fi, modern, urban, futuristic, low detailed"
    },
    {
        "name": "Game Strategy Game",
        "prompt": "strategy game style {prompt}. overhead view, detailed map, units, reminiscent of real-time strategy video games",
        "negative_prompt": "first-person view, modern, photorealistic"
    },
    {
        "name": "Game Streetfighter",
        "prompt": "Street Fighter style {prompt}. vibrant, dynamic, arcade, 2D fighting game, highly detailed, reminiscent of Street Fighter series",
        "negative_prompt": "3D, realistic, modern, photorealistic, turn-based strategy"
    },
    {
        "name": "Game Zelda",
        "prompt": "Legend of Zelda style {prompt}. vibrant, fantasy, detailed, epic, heroic, reminiscent of The Legend of Zelda series",
        "negative_prompt": "sci-fi, modern, realistic, horror"
    },
    {
        "name": "Misc Architectural",
        "prompt": "architectural style {prompt}. clean lines, geometric shapes, minimalist, modern, architectural drawing, highly detailed",
        "negative_prompt": "curved lines, ornate, baroque, abstract, grunge"
    },
    {
        "name": "Misc Disco",
        "prompt": "disco-themed {prompt}. vibrant, groovy, retro 70s style, shiny disco balls, neon lights, dance floor, highly detailed",
        "negative_prompt": "minimalist, rustic, monochrome, contemporary, simplistic"
    },
    {
        "name": "Misc Dreamscape",
        "prompt": "dreamscape {prompt}. surreal, ethereal, dreamy, mysterious, fantasy, highly detailed",
        "negative_prompt": "realistic, concrete, ordinary, mundane"
    },
    {
        "name": "Misc Dystopian",
        "prompt": "dystopian style {prompt}. bleak, post-apocalyptic, somber, dramatic, highly detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, cheerful, optimistic, vibrant, colorful"
    },
    {
        "name": "Misc Fairy Tale",
        "prompt": "fairy tale {prompt}. magical, fantastical, enchanting, storybook style, highly detailed",
        "negative_prompt": "realistic, modern, ordinary, mundane"
    },
    {
        "name": "Misc Gothic",
        "prompt": "gothic style {prompt}. dark, mysterious, haunting, dramatic, ornate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, cheerful, optimistic"
    },
    {
        "name": "Misc Grunge",
        "prompt": "grunge style {prompt}. textured, distressed, vintage, edgy, punk rock vibe, dirty, noisy",
        "negative_prompt": "smooth, clean, minimalist, sleek, modern, photorealistic"
    },
    {
        "name": "Misc Horror",
        "prompt": "horror-themed {prompt}. eerie, unsettling, dark, spooky, suspenseful, grim, highly detailed",
        "negative_prompt": "cheerful, bright, vibrant, light-hearted, cute"
    },
    {
        "name": "Misc Kawaii",
        "prompt": "kawaii style {prompt}. cute, adorable, brightly colored, cheerful, anime influence, highly detailed",
        "negative_prompt": "dark, scary, realistic, monochrome, abstract"
    },
    {
        "name": "Misc Lovecraftian",
        "prompt": "lovecraftian horror {prompt}. eldritch, cosmic horror, unknown, mysterious, surreal, highly detailed",
        "negative_prompt": "light-hearted, mundane, familiar, simplistic, realistic"
    },
    {
        "name": "Misc Macabre",
        "prompt": "macabre style {prompt}. dark, gothic, grim, haunting, highly detailed",
        "negative_prompt": "bright, cheerful, light-hearted, cartoonish, cute"
    },
    {
        "name": "Misc Manga",
        "prompt": "manga style {prompt}. vibrant, high-energy, detailed, iconic, Japanese comic style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, Western comic style"
    },
    {
        "name": "Misc Metropolis",
        "prompt": "metropolis-themed {prompt}. urban, cityscape, skyscrapers, modern, futuristic, highly detailed",
        "negative_prompt": "rural, natural, rustic, historical, simple"
    },
    {
        "name": "Misc Minimalist",
        "prompt": "minimalist style {prompt}. simple, clean, uncluttered, modern, elegant",
        "negative_prompt": "ornate, complicated, highly detailed, cluttered, disordered, messy, noisy"
    },
    {
        "name": "Misc Monochrome",
        "prompt": "monochrome {prompt}. black and white, contrast, tone, texture, detailed",
        "negative_prompt": "colorful, vibrant, noisy, blurry, deformed"
    },
    {
        "name": "Misc Nautical",
        "prompt": "nautical-themed {prompt}. sea, ocean, ships, maritime, beach, marine life, highly detailed",
        "negative_prompt": "landlocked, desert, mountains, urban, rustic"
    },
    {
        "name": "Misc Space",
        "prompt": "space-themed {prompt}. cosmic, celestial, stars, galaxies, nebulas, planets, science fiction, highly detailed",
        "negative_prompt": "earthly, mundane, ground-based, realism"
    },
    {
        "name": "Misc Stained Glass",
        "prompt": "stained glass style {prompt}. vibrant, beautiful, translucent, intricate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "Misc Techwear Fashion",
        "prompt": "techwear fashion {prompt}. futuristic, cyberpunk, urban, tactical, sleek, dark, highly detailed",
        "negative_prompt": "vintage, rural, colorful, low contrast, realism, sketch, watercolor"
    },
    {
        "name": "Misc Tribal",
        "prompt": "tribal style {prompt}. indigenous, ethnic, traditional patterns, bold, natural colors, highly detailed",
        "negative_prompt": "modern, futuristic, minimalist, pastel"
    },
    {
        "name": "Misc Zentangle",
        "prompt": "zentangle {prompt}. intricate, abstract, monochrome, patterns, meditative, highly detailed",
        "negative_prompt": "colorful, representative, simplistic, large fields of color"
    },
    {
        "name": "Papercraft Collage",
        "prompt": "collage style {prompt}. mixed media, layered, textural, detailed, artistic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "Papercraft Flat Papercut",
        "prompt": "flat papercut style {prompt}. silhouette, clean cuts, paper, sharp edges, minimalist, color block",
        "negative_prompt": "3D, high detail, noise, grainy, blurry, painting, drawing, photo, disfigured"
    },
    {
        "name": "Papercraft Kirigami",
        "prompt": "kirigami representation of {prompt}. 3D, paper folding, paper cutting, Japanese, intricate, symmetrical, precision, clean lines",
        "negative_prompt": "painting, drawing, 2D, noisy, blurry, deformed"
    },
    {
        "name": "Papercraft Paper Mache",
        "prompt": "paper mache representation of {prompt}. 3D, sculptural, textured, handmade, vibrant, fun",
        "negative_prompt": "2D, flat, photo, sketch, digital art, deformed, noisy, blurry"
    },
    {
        "name": "Papercraft Paper Quilling",
        "prompt": "paper quilling art of {prompt}. intricate, delicate, curling, rolling, shaping, coiling, loops, 3D, dimensional, ornamental",
        "negative_prompt": "photo, painting, drawing, 2D, flat, deformed, noisy, blurry"
    },
    {
        "name": "Papercraft Papercut Collage",
        "prompt": "papercut collage of {prompt}. mixed media, textured paper, overlapping, asymmetrical, abstract, vibrant",
        "negative_prompt": "photo, 3D, realistic, drawing, painting, high detail, disfigured"
    },
    {
        "name": "Papercraft Papercut Shadow Box",
        "prompt": "3D papercut shadow box of {prompt}. layered, dimensional, depth, silhouette, shadow, papercut, handmade, high contrast",
        "negative_prompt": "painting, drawing, photo, 2D, flat, high detail, blurry, noisy, disfigured"
    },
    {
        "name": "Papercraft Stacked Papercut",
        "prompt": "stacked papercut art of {prompt}. 3D, layered, dimensional, depth, precision cut, stacked layers, papercut, high contrast",
        "negative_prompt": "2D, flat, noisy, blurry, painting, drawing, photo, deformed"
    },
    {
        "name": "Papercraft Thick Layered Papercut",
        "prompt": "thick layered papercut art of {prompt}. deep 3D, volumetric, dimensional, depth, thick paper, high stack, heavy texture, tangible layers",
        "negative_prompt": "2D, flat, thin paper, low stack, smooth texture, painting, drawing, photo, deformed"
    },
    {
        "name": "Photo Alien",
        "prompt": "alien-themed {prompt}. extraterrestrial, cosmic, otherworldly, mysterious, sci-fi, highly detailed",
        "negative_prompt": "earthly, mundane, common, realistic, simple"
    },
    {
        "name": "Photo Glamour",
        "prompt": "glamorous photo {prompt}. high fashion, luxurious, extravagant, stylish, sensual, opulent, elegance, stunning beauty, professional, high contrast, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, distorted, grainy, sketch, low contrast, dull, plain, modest"
    },
    {
        "name": "Photo Hdr",
        "prompt": "HDR photo of {prompt}. High dynamic range, vivid, rich details, clear shadows and highlights, realistic, intense, enhanced contrast, highly detailed",
        "negative_prompt": "flat, low contrast, oversaturated, underexposed, overexposed, blurred, noisy"
    },
    {
        "name": "Photo Iphone Photographic",
        "prompt": "iphone photo {prompt}. large depth of field, deep depth of field, highly detailed",
        "negative_prompt": "drawing, painting, crayon, sketch, graphite, impressionist, noisy, blurry, soft, deformed, ugly, shallow depth of field, bokeh"
    },
    {
        "name": "Photo Long Exposure",
        "prompt": "long exposure photo of {prompt}. Blurred motion, streaks of light, surreal, dreamy, ghosting effect, highly detailed",
        "negative_prompt": "static, noisy, deformed, shaky, abrupt, flat, low contrast"
    },
    {
        "name": "Photo Neon Noir",
        "prompt": "neon noir {prompt}. cyberpunk, dark, rainy streets, neon signs, high contrast, low light, vibrant, highly detailed",
        "negative_prompt": "bright, sunny, daytime, low contrast, black and white, sketch, watercolor"
    },
    {
        "name": "Photo Silhouette",
        "prompt": "silhouette style {prompt}. high contrast, minimalistic, black and white, stark, dramatic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, color, realism, photorealistic"
    },
    {
        "name": "Photo Tilt Shift",
        "prompt": "tilt-shift photo of {prompt}. selective focus, miniature effect, blurred background, highly detailed, vibrant, perspective control",
        "negative_prompt": "blurry, noisy, deformed, flat, low contrast, unrealistic, oversaturated, underexposed"
    },
    {
        "name": "Cinematic Diva",
        "prompt": "UHD, 8K, ultra detailed, a cinematic photograph of {prompt}, beautiful lighting, great composition",
        "negative_prompt": "ugly, deformed, noisy, blurry, NSFW"
    },
    {
        "name": "Abstract Expressionism 2",
        "prompt": "Abstract Expressionism Art, {prompt}, High contrast, minimalistic, colorful, stark, dramatic, expressionism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "Academia",
        "prompt": "Academia, {prompt}, preppy Ivy League style, stark, dramatic, chic boarding school, academia",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, grunge, sloppy, unkempt"
    },
    {
        "name": "Action Figure",
        "prompt": "Action Figure, {prompt}, plastic collectable action figure, collectable toy action figure",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Avant Garde",
        "prompt": "Avant-garde, {prompt}, unusual, experimental, avant-garde art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Bauhaus Style Poster",
        "prompt": "Bauhaus-Style Poster, {prompt}, simple geometric shapes, clean lines, primary colors, Bauhaus-Style Poster",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Cel Shaded Art",
        "prompt": "Cel Shaded Art, {prompt}, 2D, flat color, toon shading, cel shaded style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Character Design Sheet",
        "prompt": "Character Design Sheet, {prompt}, character reference sheet, character turn around",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Color Field Painting",
        "prompt": "Color Field Painting, {prompt}, abstract, simple, geometic, color field painting style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Colored Pencil Art",
        "prompt": "Colored Pencil Art, {prompt}, colored pencil strokes, light color, visible paper texture, colored pencil art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Conceptual Art",
        "prompt": "Conceptual Art, {prompt}, concept art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Constructivism",
        "prompt": "Constructivism Art, {prompt}, minimalistic, geometric forms, constructivism art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Cubism",
        "prompt": "Cubism Art, {prompt}, flat geometric forms, cubism art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Dadaism",
        "prompt": "Dadaism Art, {prompt}, satirical, nonsensical, dadaism art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Dark Fantasy",
        "prompt": "Dark Fantasy Art, {prompt}, dark, moody, dark fantasy style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, bright, sunny"
    },
    {
        "name": "Dark Moody Atmosphere",
        "prompt": "Dark Moody Atmosphere, {prompt}, dramatic, mysterious, dark moody atmosphere",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, vibrant, colorful, bright"
    },
    {
        "name": "Dmt Art Style",
        "prompt": "DMT Art Style, {prompt}, bright colors, surreal visuals, swirling patterns, DMT art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Doodle Art",
        "prompt": "Doodle Art Style, {prompt}, drawing, freeform, swirling patterns, doodle art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Expressionism",
        "prompt": "Expressionism Art Style, {prompt}, movement, contrast, emotional, exaggerated forms, expressionism art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Faded Polaroid Photo",
        "prompt": "Faded Polaroid Photo, {prompt}, analog, old faded photo, old polaroid",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, vibrant, colorful"
    },
    {
        "name": "Fauvism",
        "prompt": "Fauvism Art, {prompt}, painterly, bold colors, textured brushwork, fauvism art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Flat 2d Art",
        "prompt": "Flat 2D Art, {prompt}, simple flat color, 2-dimensional, Flat 2D Art Style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, 3D, photo, realistic"
    },
    {
        "name": "Fortnite Art Style",
        "prompt": "Fortnite Art Style, {prompt}, 3D cartoon, colorful, Fortnite Art Style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photo, realistic"
    },
    {
        "name": "Futurism",
        "prompt": "Futurism Art Style, {prompt}, dynamic, dramatic, Futurism Art Style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Glitchcore",
        "prompt": "Glitchcore Art Style, {prompt}, dynamic, dramatic, distorted, vibrant colors, glitchcore art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Glo Fi",
        "prompt": "Glo-fi Art Style, {prompt}, dynamic, dramatic, vibrant colors, glo-fi art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Graffiti Art",
        "prompt": "Graffiti Art Style, {prompt}, dynamic, dramatic, vibrant colors, graffiti art style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Impressionism",
        "prompt": "Impressionism, {prompt}, painterly, small brushstrokes, visible brushstrokes, impressionistic style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Infographic Drawing",
        "prompt": "Infographic Drawing, {prompt}, diagram, infographic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Ink Dripping Drawing 2",
        "prompt": "Ink Dripping Drawing, {prompt}, ink drawing, dripping ink",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, colorful, vibrant"
    },
    {
        "name": "Japanese Ink Drawing 2",
        "prompt": "Japanese Ink Drawing, {prompt}, ink drawing, inkwash, Japanese Ink Drawing",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, colorful, vibrant"
    },
    {
        "name": "Logo Design",
        "prompt": "Logo Design, {prompt}, dynamic graphic art, vector art, minimalist, professional logo design",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Mandola Art",
        "prompt": "Mandola art style, {prompt}, complex, circular design, mandola",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Marker Drawing",
        "prompt": "Marker Drawing, {prompt}, bold marker lines, visibile paper texture, marker drawing",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photograph, realistic"
    },
    {
        "name": "Minimalism",
        "prompt": "Minimalism, {prompt}, abstract, simple geometic shapes, hard edges, sleek contours, Minimalism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Neo Baroque",
        "prompt": "Neo-Baroque, {prompt}, ornate and elaborate, dynaimc, Neo-Baroque",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Neo Byzantine",
        "prompt": "Neo-Byzantine, {prompt}, grand decorative religious style, Orthodox Christian inspired, Neo-Byzantine",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Neo Futurism",
        "prompt": "Neo-Futurism, {prompt}, high-tech, curves, spirals, flowing lines, idealistic future, Neo-Futurism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Neo Impressionism",
        "prompt": "Neo-Impressionism, {prompt}, tiny dabs of color, Pointillism, painterly, Neo-Impressionism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, photograph, realistic"
    },
    {
        "name": "Neo Rococo",
        "prompt": "Neo-Rococo, {prompt}, curved forms, naturalistic ornamentation, elaborate, decorative, gaudy, Neo-Rococo",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Op Art",
        "prompt": "Op Art, {prompt}, optical illusion, abstract, geometric pattern, impression of movement, Op Art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Ornate And Intricate",
        "prompt": "Ornate and Intricate, {prompt}, decorative, highly detailed, elaborate, ornate, intricate",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Pencil Sketch Drawing",
        "prompt": "Pencil Sketch Drawing, {prompt}, black and white drawing, graphite drawing",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Silhouette Art",
        "prompt": "Silhouette Art, {prompt}, high contrast, well defined, Silhouette Art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Simple Vector Art",
        "prompt": "Simple Vector Art, {prompt}, 2D flat, simple shapes, minimalistic, professional graphic, flat color, high contrast, Simple Vector Art",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, 3D, photo, realistic"
    },
    {
        "name": "Surrealism",
        "prompt": "Surrealism, {prompt}, expressive, dramatic, organic lines and forms, dreamlike and mysterious, Surrealism",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realistic"
    },
    {
        "name": "Sticker Designs",
        "prompt": "Vector Art Stickers, {prompt}, professional vector design, sticker designs, Sticker Sheet",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Vibrant Rim Light 2",
        "prompt": "Vibrant Rim Light, {prompt}, bright rim light, high contrast, bold edge light",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Volumetric Lighting",
        "prompt": "Volumetric Lighting, {prompt}, light depth, dramatic atmospheric lighting, Volumetric Lighting",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast"
    },
    {
        "name": "Mk Chromolithography",
        "prompt": "Chromolithograph {prompt}. Vibrant colors, intricate details, rich color saturation, meticulous registration, multi-layered printing, decorative elements, historical charm, artistic reproductions, commercial posters, nostalgic, ornate compositions.",
        "negative_prompt": "monochromatic, simple designs, limited color palette, imprecise registration, minimalistic, modern aesthetic, digital appearance."
    },
    {
        "name": "Mk Cross Processing Print",
        "prompt": "Cross processing print {prompt}. Experimental color shifts, unconventional tonalities, vibrant and surreal hues, heightened contrasts, unpredictable results, artistic unpredictability, retro and vintage feel, dynamic color interplay, abstract and dreamlike.",
        "negative_prompt": "predictable color tones, traditional processing, realistic color representation, subdued contrasts, standard photographic aesthetics."
    },
    {
        "name": "Mk Dufaycolor Photograph",
        "prompt": "Dufaycolor photograph {prompt}. Vintage color palette, distinctive color rendering, soft and dreamy atmosphere, historical charm, unique color process, grainy texture, evocative mood, nostalgic aesthetic, hand-tinted appearance, artistic patina.",
        "negative_prompt": "modern color reproduction, hyperrealistic tones, sharp and clear details, digital precision, contemporary aesthetic."
    },
    {
        "name": "Mk Herbarium",
        "prompt": "Herbarium drawing {prompt}. Botanical accuracy, old botanical book illustration, detailed illustrations, pressed plants, delicate and precise linework, scientific documentation, meticulous presentation, educational purpose, organic compositions, timeless aesthetic, naturalistic beauty.",
        "negative_prompt": "abstract representation, vibrant colors, artistic interpretation, chaotic compositions, fantastical elements, digital appearance."
    },
    {
        "name": "Mk Punk Collage",
        "prompt": "punk collage style {prompt}. mixed media, papercut,textured paper, overlapping, ripped posters, safety pins, chaotic layers, graffiti-style elements, anarchy symbols, vintage photos, cut-and-paste aesthetic, bold typography, distorted images, political messages, urban decay, distressed textures, newspaper clippings, spray paint, rebellious icons, DIY spirit, vivid colors, punk band logos, edgy and raw compositions,",
        "negative_prompt": "conventional,blurry, noisy, low contrast"
    },
    {
        "name": "Mk Mosaic",
        "prompt": "mosaic style {prompt}. fragmented, assembled, colorful, highly detailed",
        "negative_prompt": "whole, unbroken, monochrome"
    },
    {
        "name": "Mk Van Gogh",
        "prompt": "Oil painting by Van Gogh {prompt}. Expressive, impasto, swirling brushwork, vibrant, brush strokes, Brushstroke-heavy, Textured, Impasto, Colorful, Dynamic, Bold, Distinctive, Vibrant, Whirling, Expressive, Dramatic, Swirling, Layered, Intense, Contrastive, Atmospheric, Luminous, Textural, Evocative, SpiraledVan Gogh style",
        "negative_prompt": "realistic, photorealistic, calm, straight lines, signature, frame, text, watermark"
    },
    {
        "name": "Mk Coloring Book",
        "prompt": "centered black and white high contrast line drawing, coloring book style, {prompt}. monochrome, blank white background",
        "negative_prompt": "greyscale, gradients,shadows,shadow, colored, Red, Blue, Yellow, Green, Orange, Purple, Pink, Brown, Gray, Beige, Turquoise, Lavender, Cyan, Magenta, Olive, Indigo, black background"
    },
    {
        "name": "Mk Singer Sargent",
        "prompt": "Oil painting by John Singer Sargent {prompt}. Elegant, refined, masterful technique,realistic portrayal, subtle play of light, captivating expression, rich details, harmonious colors, skillful composition, brush strokes, chiaroscuro.",
        "negative_prompt": "realistic, photorealistic, abstract, overly stylized, excessive contrasts, distorted,bright colors,disorder."
    },
    {
        "name": "Mk Pollock",
        "prompt": "Oil painting by Jackson Pollock {prompt}. Abstract expressionism, drip painting, chaotic composition, energetic, spontaneous, unconventional technique, dynamic, bold, distinctive, vibrant, intense, expressive, energetic, layered, non-representational, gestural.",
        "negative_prompt": "(realistic:1.5), (photorealistic:1.5), representational, calm, ordered composition, precise lines, detailed forms, subdued colors, quiet, static, traditional, figurative."
    },
    {
        "name": "Mk Basquiat",
        "prompt": "Artwork by Jean-Michel Basquiat {prompt}. Neo-expressionism, street art influence, graffiti-inspired, raw, energetic, bold colors, dynamic composition, chaotic, layered, textural, expressive, spontaneous, distinctive, symbolic,energetic brushstrokes.",
        "negative_prompt": "(realistic:1.5), (photorealistic:1.5), calm, precise lines, conventional composition, subdued"
    },
    {
        "name": "Mk Andy Warhol",
        "prompt": "Artwork in the style of Andy Warhol {prompt}. Pop art, vibrant colors, bold compositions, repetition of iconic imagery, celebrity culture, commercial aesthetics, mass production influence, stylized simplicity, cultural commentary, graphical elements, distinctive portraits.",
        "negative_prompt": "subdued colors, realistic, lack of repetition, minimalistic."
    },
    {
        "name": "Mk Halftone Print",
        "prompt": "Halftone print of {prompt}. Dot matrix pattern, grayscale tones, vintage aesthetic, newspaper print vibe, stylized dots, visual texture, black and white contrasts, retro appearance, artistic pointillism,pop culture, (Roy Lichtenstein style:1.5).",
        "negative_prompt": "smooth gradients, continuous tones, vibrant colors."
    },
    {
        "name": "Mk Gond Painting",
        "prompt": "Gond painting {prompt}. Intricate patterns, vibrant colors, detailed motifs, nature-inspired themes, tribal folklore, fine lines, intricate detailing, storytelling compositions, mystical and folkloric, cultural richness.",
        "negative_prompt": "monochromatic, abstract shapes, minimalistic."
    },
    {
        "name": "Mk Albumen Print",
        "prompt": "Albumen print {prompt}. Sepia tones, fine details, subtle tonal gradations, delicate highlights, vintage aesthetic, soft and muted atmosphere, historical charm, rich textures, meticulous craftsmanship, classic photographic technique, vignetting.",
        "negative_prompt": "vibrant colors, high contrast, modern, digital appearance, sharp details, contemporary style."
    },
    {
        "name": "Mk Aquatint Print",
        "prompt": "Aquatint print {prompt}. Soft tonal gradations, atmospheric effects, velvety textures, rich contrasts, fine details, etching process, delicate lines, nuanced shading, expressive and moody atmosphere, artistic depth.",
        "negative_prompt": "sharp contrasts, bold lines, minimalistic."
    },
    {
        "name": "Mk Anthotype Print",
        "prompt": "Anthotype print {prompt}. Monochrome dye, soft and muted colors, organic textures, ephemeral and delicate appearance, low details, watercolor canvas, low contrast, overexposed, silhouette, textured paper.",
        "negative_prompt": "vibrant synthetic dyes, bold and saturated colors."
    },
    {
        "name": "Mk Inuit Carving",
        "prompt": "A sculpture made of ivory, {prompt} made of . Sculptures, Inuit art style, intricate carvings, natural materials, storytelling motifs, arctic wildlife themes, symbolic representations, cultural traditions, earthy tones, harmonious compositions, spiritual and mythological elements.",
        "negative_prompt": "abstract, vibrant colors."
    },
    {
        "name": "Mk Bromoil Print",
        "prompt": "Bromoil print {prompt}. Painterly effects, sepia tones, textured surfaces, rich contrasts, expressive brushwork, tonal variations, vintage aesthetic, atmospheric mood, handmade quality, artistic experimentation, darkroom craftsmanship, vignetting.",
        "negative_prompt": "smooth surfaces, minimal brushwork, contemporary digital appearance."
    },
    {
        "name": "Mk Calotype Print",
        "prompt": "Calotype print {prompt}. Soft focus, subtle tonal range, paper negative process, fine details, vintage aesthetic, artistic experimentation, atmospheric mood, early photographic charm, handmade quality, vignetting.",
        "negative_prompt": "sharp focus, bold contrasts, modern aesthetic, digital photography."
    },
    {
        "name": "Mk Color Sketchnote",
        "prompt": "Color sketchnote {prompt}. Hand-drawn elements, vibrant colors, visual hierarchy, playful illustrations, varied typography, graphic icons, organic and dynamic layout, personalized touches, creative expression, engaging storytelling.",
        "negative_prompt": "monochromatic, geometric layout."
    },
    {
        "name": "Mk Cibulak Porcelain",
        "prompt": "A sculpture made of blue pattern porcelain of {prompt}. Classic design, blue and white color scheme, intricate detailing, floral motifs, onion-shaped elements, historical charm, rococo, white ware, cobalt blue, underglaze pattern, fine craftsmanship, traditional elegance, delicate patterns, vintage aesthetic, Meissen, Blue Onion pattern, Cibulak.",
        "negative_prompt": "tea, teapot, cup, teacup,bright colors, bold and modern design, absence of intricate detailing, lack of floral motifs, non-traditional shapes."
    },
    {
        "name": "Mk Alcohol Ink Art",
        "prompt": "Alcohol ink art {prompt}. Fluid and vibrant colors, unpredictable patterns, organic textures, translucent layers, abstract compositions, ethereal and dreamy effects, free-flowing movement, expressive brushstrokes, contemporary aesthetic, wet textured paper.",
        "negative_prompt": "monochromatic, controlled patterns."
    },
    {
        "name": "Mk One Line Art",
        "prompt": "One line art {prompt}. Continuous and unbroken black line, minimalistic, simplicity, economical use of space, flowing and dynamic, symbolic representations, contemporary aesthetic, evocative and abstract, white background.",
        "negative_prompt": "disjointed lines, complexity, complex detailing."
    },
    {
        "name": "Mk Blacklight Paint",
        "prompt": "Blacklight paint {prompt}. Fluorescent pigments, vibrant and surreal colors, ethereal glow, otherworldly effects, dynamic and psychedelic compositions, neon aesthetics, transformative in ultraviolet light, contemporary and experimental.",
        "negative_prompt": "muted colors, traditional and realistic compositions."
    },
    {
        "name": "Mk Carnival Glass",
        "prompt": "A sculpture made of Carnival glass, {prompt}. Iridescent surfaces, vibrant colors, intricate patterns, opalescent hues, reflective and prismatic effects, Art Nouveau and Art Deco influences, vintage charm, intricate detailing, lustrous and luminous appearance, Carnival Glass style.",
        "negative_prompt": "non-iridescent surfaces, muted colors, absence of intricate patterns, lack of opalescent hues, modern and minimalist aesthetic."
    },
    {
        "name": "Mk Cyanotype Print",
        "prompt": "Cyanotype print {prompt}. Prussian blue tones, distinctive coloration, high contrast, blueprint aesthetics, atmospheric mood, sun-exposed paper, silhouette effects, delicate details, historical charm, handmade and experimental quality.",
        "negative_prompt": "vibrant colors, low contrast, modern and polished appearance."
    },
    {
        "name": "Mk Cross Stitching",
        "prompt": "Cross-stitching {prompt}. Intricate patterns, embroidery thread, sewing, fine details, precise stitches, textile artistry, symmetrical designs, varied color palette, traditional and contemporary motifs, handmade and crafted,canvas, nostalgic charm.",
        "negative_prompt": "paper, paint, ink, photography."
    },
    {
        "name": "Mk Encaustic Paint",
        "prompt": "Encaustic paint {prompt}. Textured surfaces, translucent layers, luminous quality, wax medium, rich color saturation, fluid and organic shapes, contemporary and historical influences, mixed media elements, atmospheric depth.",
        "negative_prompt": "flat surfaces, opaque layers, lack of wax medium, muted color palette, absence of textured surfaces, non-mixed media."
    },
    {
        "name": "Mk Embroidery",
        "prompt": "Embroidery {prompt}. Intricate stitching, embroidery thread, fine details, varied thread textures, textile artistry, embellished surfaces, diverse color palette, traditional and contemporary motifs, handmade and crafted, tactile and ornate.",
        "negative_prompt": "minimalist, monochromatic."
    },
    {
        "name": "Mk Gyotaku",
        "prompt": "Gyotaku {prompt}. Fish impressions, realistic details, ink rubbings, textured surfaces, traditional Japanese art form, nature-inspired compositions, artistic representation of marine life, black and white contrasts, cultural significance.",
        "negative_prompt": "photography."
    },
    {
        "name": "Mk Luminogram",
        "prompt": "Luminogram {prompt}. Photogram technique, ethereal and abstract effects, light and shadow interplay, luminous quality, experimental process, direct light exposure, unique and unpredictable results, artistic experimentation.",
        "negative_prompt": ""
    },
    {
        "name": "Mk Lite Brite Art",
        "prompt": "Lite Brite art {prompt}. Luminous and colorful designs, pixelated compositions, retro aesthetic, glowing effects, creative patterns, interactive and playful, nostalgic charm, vibrant and dynamic arrangements.",
        "negative_prompt": "monochromatic."
    },
    {
        "name": "Mk Mokume Gane",
        "prompt": "Mokume-gane {prompt}. Wood-grain patterns, mixed metal layers, intricate and organic designs, traditional Japanese metalwork, harmonious color combinations, artisanal craftsmanship, unique and layered textures, cultural and historical significance.",
        "negative_prompt": "uniform metal surfaces."
    },
    {
        "name": "Pebble Art",
        "prompt": "a sculpture made of peebles, {prompt}. Pebble art style,natural materials, textured surfaces, balanced compositions, organic forms, harmonious arrangements, tactile and 3D effects, beach-inspired aesthetic, creative storytelling, artisanal craftsmanship.",
        "negative_prompt": "non-natural materials, lack of textured surfaces, imbalanced compositions, absence of organic forms, non-tactile appearance."
    },
    {
        "name": "Mk Palekh",
        "prompt": "Palekh art {prompt}. Miniature paintings, intricate details, vivid colors, folkloric themes, lacquer finish, storytelling compositions, symbolic elements, Russian folklore influence, cultural and historical significance.",
        "negative_prompt": "large-scale paintings."
    },
    {
        "name": "Mk Suminagashi",
        "prompt": "Suminagashi {prompt}. Floating ink patterns, marbled effects, delicate and ethereal designs, water-based ink, fluid and unpredictable compositions, meditative process, monochromatic or subtle color palette, Japanese artistic tradition.",
        "negative_prompt": "vibrant and bold color palette."
    },
    {
        "name": "Mk Scrimshaw",
        "prompt": "A Scrimshaw engraving of {prompt}. Intricate engravings on a spermwhale's teeth, marine motifs, detailed scenes, nautical themes, black and white contrasts, historical craftsmanship, artisanal carving, storytelling compositions, maritime heritage.",
        "negative_prompt": "colorful, modern."
    },
    {
        "name": "Mk Shibori",
        "prompt": "Shibori {prompt}. Textured fabric, intricate patterns, resist-dyeing technique, indigo or vibrant colors, organic and flowing designs, Japanese textile art, cultural tradition, tactile and visual interest.",
        "negative_prompt": "monochromatic."
    },
    {
        "name": "Mk Vitreous Enamel",
        "prompt": "A sculpture made of Vitreous enamel {prompt}. Smooth and glossy surfaces, vibrant colors, glass-like finish, durable and resilient, intricate detailing, traditional and contemporary applications, artistic craftsmanship, jewelry and decorative objects, , Vitreous enamel, colored glass.",
        "negative_prompt": "rough surfaces, muted colors."
    },
    {
        "name": "Mk Ukiyo E",
        "prompt": "Ukiyo-e {prompt}. Woodblock prints, vibrant colors, intricate details, depictions of landscapes, kabuki actors, beautiful women, cultural scenes, traditional Japanese art, artistic craftsmanship, historical significance.",
        "negative_prompt": "absence of woodblock prints, muted colors, lack of intricate details, non-traditional Japanese themes, absence of cultural scenes."
    },
    {
        "name": "Mk Vintage Airline Poster",
        "prompt": "vintage airline poster {prompt}. classic aviation fonts, pastel colors, elegant aircraft illustrations, scenic destinations, distressed textures, retro travel allure",
        "negative_prompt": "modern fonts, bold colors, hyper-realistic, sleek design"
    },
    {
        "name": "Mk Vintage Travel Poster",
        "prompt": "vintage travel poster {prompt}. retro fonts, muted colors, scenic illustrations, iconic landmarks, distressed textures, nostalgic vibes",
        "negative_prompt": "modern fonts, vibrant colors, hyper-realistic, sleek design"
    },
    {
        "name": "Mk Bauhaus Style",
        "prompt": "Bauhaus-inspired {prompt}. minimalism, geometric precision, primary colors, sans-serif typography, asymmetry, functional design",
        "negative_prompt": "ornate, intricate, excessive detail, complex patterns, serif typography"
    },
    {
        "name": "Mk Afrofuturism",
        "prompt": "Afrofuturism illustration {prompt}. vibrant colors, futuristic elements, cultural symbolism, cosmic imagery, dynamic patterns, empowering narratives",
        "negative_prompt": "monochromatic"
    },
    {
        "name": "Mk Atompunk",
        "prompt": "Atompunk illustation, {prompt}. retro-futuristic, atomic age aesthetics, sleek lines, metallic textures, futuristic technology, optimism, energy",
        "negative_prompt": "organic, natural textures, rustic, dystopian"
    },
    {
        "name": "Mk Constructivism",
        "prompt": "Constructivism {prompt}. geometric abstraction, bold colors, industrial aesthetics, dynamic compositions, utilitarian design, revolutionary spirit",
        "negative_prompt": "organic shapes, muted colors, ornate elements, traditional"
    },
    {
        "name": "Mk Chicano Art",
        "prompt": "Chicano art {prompt}. bold colors, cultural symbolism, muralism, lowrider aesthetics, barrio life, political messages, social activism, Mexico",
        "negative_prompt": "monochromatic, minimalist, mainstream aesthetics"
    },
    {
        "name": "Mk De Stijl",
        "prompt": "De Stijl Art {prompt}. neoplasticism, primary colors, geometric abstraction, horizontal and vertical lines, simplicity, harmony, utopian ideals",
        "negative_prompt": "complex patterns, muted colors, ornate elements, asymmetry"
    },
    {
        "name": "Mk Dayak Art",
        "prompt": "Dayak art sculpture of {prompt}. intricate patterns, nature-inspired motifs, vibrant colors, traditional craftsmanship, cultural symbolism, storytelling",
        "negative_prompt": "minimalist, monochromatic, modern"
    },
    {
        "name": "Mk Fayum Portrait",
        "prompt": "Fayum portrait {prompt}. encaustic painting, realistic facial features, warm earth tones, serene expressions, ancient Egyptian influences",
        "negative_prompt": "abstract, vibrant colors, exaggerated features, modern"
    },
    {
        "name": "Mk Illuminated Manuscript",
        "prompt": "Illuminated manuscript {prompt}. intricate calligraphy, rich colors, detailed illustrations, gold leaf accents, ornate borders, religious, historical, medieval",
        "negative_prompt": "modern typography, minimalist design, monochromatic, abstract themes"
    },
    {
        "name": "Mk Kalighat Painting",
        "prompt": "Kalighat painting {prompt}. bold lines, vibrant colors, narrative storytelling, cultural motifs, flat compositions, expressive characters",
        "negative_prompt": "subdued colors, intricate details, realistic portrayal, modern aesthetics"
    },
    {
        "name": "Mk Madhubani Painting",
        "prompt": "Madhubani painting {prompt}. intricate patterns, vibrant colors, nature-inspired motifs, cultural storytelling, symmetry, folk art aesthetics",
        "negative_prompt": "abstract, muted colors, minimalistic design, modern aesthetics"
    },
    {
        "name": "Mk Pictorialism",
        "prompt": "Pictorialism illustration {prompt}. soft focus, atmospheric effects, artistic interpretation, tonality, muted colors, evocative storytelling",
        "negative_prompt": "sharp focus, high contrast, realistic depiction, vivid colors"
    },
    {
        "name": "Mk Pichwai Painting",
        "prompt": "Pichwai painting {prompt}. intricate detailing, vibrant colors, religious themes, nature motifs, devotional storytelling, gold leaf accents",
        "negative_prompt": "minimalist, subdued colors, abstract design"
    },
    {
        "name": "Mk Patachitra Painting",
        "prompt": "Patachitra painting {prompt}. bold outlines, vibrant colors, intricate detailing, mythological themes, storytelling, traditional craftsmanship",
        "negative_prompt": "subdued colors, minimalistic, abstract, modern aesthetics"
    },
    {
        "name": "Mk Samoan Art Inspired",
        "prompt": "Samoan art-inspired wooden sculpture {prompt}. traditional motifs, natural elements, bold colors, cultural symbolism, storytelling, craftsmanship",
        "negative_prompt": "modern aesthetics, minimalist, abstract"
    },
    {
        "name": "Mk Tlingit Art",
        "prompt": "Tlingit art {prompt}. formline design, natural elements, animal motifs, bold colors, cultural storytelling, traditional craftsmanship, Alaska traditional art, (totem:1.5)",
        "negative_prompt": ""
    },
    {
        "name": "Mk Adnate Style",
        "prompt": "Painting by Adnate {prompt}. realistic portraits, street art, large-scale murals, subdued color palette, social narratives",
        "negative_prompt": "abstract, vibrant colors, small-scale art"
    },
    {
        "name": "Mk Ron English Style",
        "prompt": "Painting by Ron English {prompt}. pop-surrealism, cultural subversion, iconic mash-ups, vibrant and bold colors, satirical commentary",
        "negative_prompt": "traditional, monochromatic"
    },
    {
        "name": "Mk Shepard Fairey Style",
        "prompt": "Painting by Shepard Fairey {prompt}. street art, political activism, iconic stencils, bold typography, high contrast, red, black, and white color palette",
        "negative_prompt": "traditional, muted colors"
    }
]

styles = {k["name"]: (k["prompt"], k["negative_prompt"]) for k in style_list}