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
        "name": "ads-luxury",
        "prompt": "luxury product style, {prompt}, elegant, sophisticated, high-end, luxurious, professional, highly detailed",
        "negative_prompt": "cheap, noisy, blurry, unattractive, amateurish"
    },
    {
        "name": "ads-retail",
        "prompt": "retail packaging style, {prompt}, vibrant, enticing, commercial, product-focused, eye-catching, professional, highly detailed",
        "negative_prompt": "noisy, blurry, amateurish, sloppy, unattractive"
    },
    {
        "name": "img2img 3d to photorealisim",
        "prompt": "RAW photo, (high detailed skin:1.2), 8k uhd, dslr, soft lighting, high quality, film grain, Fujifilm XT3",
        "negative_prompt": "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.2), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck"
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
        "name": "Ads Gourmet Food Photography",
        "prompt": "gourmet food photo of {prompt}. soft natural lighting, macro details, vibrant colors, fresh ingredients, glistening textures, bokeh background, styled plating, wooden tabletop, garnished, tantalizing, editorial quality",
        "negative_prompt": "cartoon, anime, sketch, grayscale, dull, overexposed, cluttered, messy plate, deformed"
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
    },
    {
        "name": "Photographic — Golden Hour",
        "prompt": "golden hour cinematic photo {prompt}, 35mm, shallow depth of field, warm rim light, film grain, bokeh, professional, ultra detailed",
        "negative_prompt": "lowres, low quality, worst quality, watermark, text, blurry, deformed, ugly",
    },
    {
        "name": "Photographic — 35mm Portrait",
        "prompt": "studio 35mm portrait of {prompt}, cinematic lighting, film emulation, shallow DOF, Kodak Portra aesthetic, highly detailed",
        "negative_prompt": "drawing, painting, cartoon, lowres, watermark, text, out of focus, deformed",
    },
    {
        "name": "Cinematic — Anamorphic Blockbuster",
        "prompt": "epic anamorphic cinematic shot of {prompt}, huge depth, lens flare, volumetric light, Dolby Vision cinematic grading, ultra detailed",
        "negative_prompt": "lowres, watermark, text, cartoon, sketch, blurry, dull",
    },
    {
        "name": "Neon — Cyberpunk",
        "prompt": "neon cyberpunk scene {prompt}, rainy streets, vibrant magenta and cyan, reflective wet pavement, cinematic camera, detailed cityscape",
        "negative_prompt": "lowres, low quality, worst quality, watermark, text, deformed, blurry",
    },
    {
        "name": "Synthwave — 80s Retro",
        "prompt": "synthwave 80s retro {prompt}, neon grid, sunset gradient, vintage film, VHS artifacts, stylized, high saturation",
        "negative_prompt": "lowres, watermark, text, modern UI, realistic photography, dull",
    },
    {
        "name": "Photorealism — Hyperreal Portrait",
        "prompt": "ultra photorealistic portrait of {prompt}, 85mm, perfect skin detail, subsurface scattering, studio lighting, ultra high resolution",
        "negative_prompt": "painting, sketch, cartoon, lowres, blurry, deformed, ugly",
    },
    {
        "name": "Watercolor — Soft Wash",
        "prompt": "watercolor painting of {prompt}, soft washes, bleeding pigments, paper texture, delicate edges, dreamy atmosphere, high detail",
        "negative_prompt": "photograph, lowres, text, watermark, vector, sharp outlines",
    },
    {
        "name": "Oil Painting — Classical",
        "prompt": "oil painting, classical style {prompt}, rich impasto brushwork, Rembrandt lighting, canvas texture, museum quality",
        "negative_prompt": "digital art, lowres, watermark, text, sketchy, blurry",
    },
    {
        "name": "Gouache Illustration",
        "prompt": "gouache illustration of {prompt}, flat layered colors, visible brush strokes, stylized, editorial children book vibe",
        "negative_prompt": "photorealistic, lowres, watermark, text, noisy",
    },
    {
        "name": "Ukiyo-e — Japanese Woodblock",
        "prompt": "ukiyo-e woodblock print style {prompt}, flattened perspective, strong line art, traditional palette, Japanese patterns",
        "negative_prompt": "photorealistic, modern, lowres, watermark, text, blurry",
    },
    {
        "name": "Pixel Art — 16-bit",
        "prompt": "pixel art 16-bit {prompt}, limited palette, retro game sprite, crisp pixels, isometric or side-view, charming",
        "negative_prompt": "photorealistic, highres, blur, watermark, text",
    },
    {
        "name": "Vector — Clean Line Art",
        "prompt": "clean vector illustration of {prompt}, crisp lines, flat shapes, scalable, editorial graphic style, minimal shading",
        "negative_prompt": "photorealistic, lowres, textured brush, watermark",
    },
    {
        "name": "Comic Book — Inks & Halftone",
        "prompt": "comic book art of {prompt}, strong inks, halftone dots, dynamic pose, panel-ready composition, high contrast",
        "negative_prompt": "photo, lowres, watercolor, blurry, watermark",
    },
    {
        "name": "Manga — Shonen",
        "prompt": "manga style {prompt}, shonen action, dynamic speed lines, expressive face, screentone shading, crisp linework",
        "negative_prompt": "photorealistic, lowres, color film, watermark, text",
    },
    {
        "name": "Children's Book — Whimsical",
        "prompt": "whimsical children's book illustration of {prompt}, soft textures, playful characters, warm palette, inviting composition",
        "negative_prompt": "dark, photorealistic, lowres, watermark, text",
    },
    {
        "name": "Low Poly 3D",
        "prompt": "low poly 3D render of {prompt}, stylized geometric shapes, flat shading, game asset ready, crisp silhouettes",
        "negative_prompt": "photorealistic, high poly, noisy textures, watermark",
    },
    {
        "name": "Voxel Art",
        "prompt": "voxel art style {prompt}, blocky isometric look, game aesthetic, bright color blocks, simple lighting",
        "negative_prompt": "smooth, photorealistic, lowres, watermark",
    },
    {
        "name": "Paper Cut Collage",
        "prompt": "paper cut collage {prompt}, layered paper textures, drop shadows, tactile feel, handcrafted look",
        "negative_prompt": "photorealistic, lowres, watermark, text",
    },
    {
        "name": "Concept Art — Matte Painting",
        "prompt": "concept matte painting of {prompt}, expansive vistas, cinematic composition, photobashed realism, high detail",
        "negative_prompt": "cartoon, lowres, watermark, text, noisy",
    },
    {
        "name": "3D Render — Octane",
        "prompt": "photorealistic 3D render of {prompt}, octane style, PBR materials, soft global illumination, studio HDRI, ultra detailed",
        "negative_prompt": "sketch, lowres, watercolor, cartoon, watermark",
    },
    {
        "name": "3D Render — Unreal Engine Cinematic",
        "prompt": "unreal engine cinematic render of {prompt}, filmic post-processing, depth of field, volumetric fog, photoreal realism",
        "negative_prompt": "cartoon, lowres, sketchy, watermark",
    },
    {
        "name": "HDR Landscape",
        "prompt": "high dynamic range landscape of {prompt}, ultra wide angle, dramatic skies, rich colors, crisp details",
        "negative_prompt": "lowres, painting, watercolor, watermark, text",
    },
    {
        "name": "Macro — Insect & Detail",
        "prompt": "macro photography {prompt}, extreme close-up, high detail, shallow DOF, Nikon micro lens, textured detail",
        "negative_prompt": "wide shot, lowres, painting, cartoon, watermark",
    },
    {
        "name": "Astrophotography",
        "prompt": "astrophotography of {prompt}, star trails, Milky Way, long exposure, high ISO detail, crisp night sky",
        "negative_prompt": "daylight, lowres, noisy, watermark",
    },
    {
        "name": "Aerial Drone",
        "prompt": "aerial drone shot of {prompt}, top-down composition, sweeping landscape, cinematic gradings, high altitude clarity",
        "negative_prompt": "close-up, lowres, painting, watermark",
    },
    {
        "name": "Tilt-Shift Miniature",
        "prompt": "tilt-shift miniature effect of {prompt}, shallow band of focus, miniature toy-like scale, bright colors",
        "negative_prompt": "full sharpness, lowres, watermark, text",
    },
    {
        "name": "Long Exposure — Light Trails",
        "prompt": "long exposure light trails around {prompt}, motion blur, smooth water, silky clouds, slow shutter look",
        "negative_prompt": "freezing action, lowres, cartoon, watermark",
    },
    {
        "name": "Infrared Surreal",
        "prompt": "infrared photography look for {prompt}, surreal foliage, false-color swap, high contrast, dreamlike",
        "negative_prompt": "natural color, lowres, watermark, text",
    },
    {
        "name": "Polaroid Instant",
        "prompt": "polaroid instant photo of {prompt}, square frame, soft colors, slight vignette, instant film grain",
        "negative_prompt": "high definition, digital, watermark, text",
    },
    {
        "name": "Tilted Frame — Dynamic Crop",
        "prompt": "dynamic tilted framing of {prompt}, off-kilter composition, dramatic crop, high energy, editorial photography",
        "negative_prompt": "static centered, lowres, watermark",
    },
    {
        "name": "Monochrome Minimal",
        "prompt": "monochrome minimal {prompt}, high contrast black and white, negative space, editorial elegance",
        "negative_prompt": "colorful, cluttered, lowres, watermark",
    },
    {
        "name": "High Fashion Editorial",
        "prompt": "high fashion editorial shoot of {prompt}, dramatic styling, couture wardrobe, studio strobes, glossy magazine finish",
        "negative_prompt": "casual, lowres, messy, watermark",
    },
    {
        "name": "Surrealist Dali",
        "prompt": "surrealist painting in the spirit of Dali for {prompt}, melting forms, dream logic, uncanny juxtaposition, painterly detail",
        "negative_prompt": "photorealistic, lowres, watermark, text",
    },
    {
        "name": "Magic Realism",
        "prompt": "magic realism depiction of {prompt}, grounded detail with a single fantastic element, soft cinematic lighting, painterly",
        "negative_prompt": "cartoonish, lowres, watermark, text",
    },
    {
        "name": "Baroque Oil Portrait",
        "prompt": "baroque oil portrait of {prompt}, dramatic chiaroscuro, ornate fabrics, rich color palette, museum painting realism",
        "negative_prompt": "modern, lowres, cartoon, watermark",
    },
    {
        "name": "Impressionist Brushwork",
        "prompt": "impressionist painting of {prompt}, loose brushwork, visible paint strokes, vibrant color, plein air feel",
        "negative_prompt": "photorealistic, lowres, watermark, text",
    },
    {
        "name": "Expressionist — Emotional Color",
        "prompt": "expressionist painting {prompt}, bold unnatural colors, energetic brush marks, emotional intensity",
        "negative_prompt": "photorealistic, lowres, watermark",
    },
    {
        "name": "Minimal Line Art",
        "prompt": "minimal continuous line drawing of {prompt}, elegant simplicity, negative space, gallery print quality",
        "negative_prompt": "photorealistic, detailed shading, lowres, watermark",
    },
    {
        "name": "Silhouette — Backlit",
        "prompt": "backlit silhouette of {prompt}, high contrast rim light, simplified shape language, dramatic sky",
        "negative_prompt": "flat lighting, lowres, watermark, text",
    },
    {
        "name": "Collage — Mixed Media",
        "prompt": "mixed media collage of {prompt}, paper textures, scanned materials, layered ephemera, tactile detail",
        "negative_prompt": "digital flatness, lowres, watermark",
    },
    {
        "name": "Stipple Engraving",
        "prompt": "stipple engraving illustration of {prompt}, etched dots and lines, antique print aesthetic, high contrast detail",
        "negative_prompt": "smooth gradients, color, lowres, watermark",
    },
    {
        "name": "Pen & Ink Crosshatch",
        "prompt": "pen and ink crosshatch drawing of {prompt}, dense textures, dramatic shading, classic illustration",
        "negative_prompt": "soft brushes, watercolor, color, lowres",
    },
    {
        "name": "Retro Poster — Art Deco",
        "prompt": "art deco retro poster {prompt}, geometric ornament, gold accents, stylized figures, vintage typography suggestion",
        "negative_prompt": "photorealistic, lowres, watermark, modern UI",
    },
    {
        "name": "Surreal Collage — Photomontage",
        "prompt": "surreal photomontage of {prompt}, convincing cuts, mismatched scales, uncanny composition, editorial surrealism",
        "negative_prompt": "clean realism, lowres, watermark, text",
    },
    {
        "name": "Hyper Stylized — Comic Pop",
        "prompt": "pop art comic style {prompt}, bold flat color, halftone texture, speech bubble suggestion, high contrast",
        "negative_prompt": "photorealistic, lowres, watercolor, watermark",
    },
    {
        "name": "Fantasy — High Fantasy Painting",
        "prompt": "high fantasy painting of {prompt}, grand vistas, ornate armor, dramatic skies, painterly brushwork, cinematic lighting",
        "negative_prompt": "modern clothing, lowres, watermark",
    },
    {
        "name": "Dark Fantasy — Grimdark",
        "prompt": "grimdark fantasy {prompt}, bleak palette, heavy atmosphere, ominous figures, textured brushwork",
        "negative_prompt": "bright cheerful, lowres, watermark",
    },
    {
        "name": "Sci‑Fi — Space Opera",
        "prompt": "space opera scene of {prompt}, colossal ships, cosmic vistas, neon thrusters, cinematic scale",
        "negative_prompt": "domestic scene, lowres, watercolor, watermark",
    },
    {
        "name": "Cyber Organic — Biopunk",
        "prompt": "biopunk cyber-organic {prompt}, bio-luminescent veins, biotech implants, wet reflective surfaces, gritty detail",
        "negative_prompt": "clean, lowres, watermark, text",
    },
    {
        "name": "Steampunk — Victorian Machinery",
        "prompt": "steampunk Victorian machinery surrounds {prompt}, brass gears, steam, intricate contraptions, smoky atmosphere",
        "negative_prompt": "modern electronics, lowres, watermark",
    },
    {
        "name": "Architectural — Brutalist",
        "prompt": "brutalist architecture photo of {prompt}, strong concrete forms, dramatic geometry, stark contrast, editorial city photography",
        "negative_prompt": "lush greenery, lowres, watercolor, cartoon",
    },
    {
        "name": "Architectural — Gothic Cathedra",
        "prompt": "gothic cathedral interior around {prompt}, soaring arches, stained glass light shafts, ornate stonework, moody atmosphere",
        "negative_prompt": "modern minimal, lowres, cartoon",
    },
    {
        "name": "Fashion Illustration — Runway Sketch",
        "prompt": "fashion runway sketch of {prompt}, elongated proportions, gestural lines, fabric suggestion, couture vibe",
        "negative_prompt": "photorealistic, lowres, watermark",
    },
    {
        "name": "Food Photography — Editorial",
        "prompt": "editorial food photography of {prompt}, styled plating, shallow DOF, natural light, mouthwatering detail",
        "negative_prompt": "messy, lowres, watercolor, cartoon",
    },
    {
        "name": "Product Shot — Minimal",
        "prompt": "minimal product shot of {prompt}, clean studio, white seamless background, soft shadows, glossy reflection",
        "negative_prompt": "busy background, lowres, watercolor, text",
    },
    {
        "name": "Posterized — High Contrast",
        "prompt": "posterized high contrast {prompt}, simplified tonal regions, bold graphic impact, striking composition",
        "negative_prompt": "soft gradients, lowres, watermark",
    },
    {
        "name": "Double Exposure 2",
        "prompt": "double exposure portrait of {prompt}, layered landscapes and portrait silhouette, dreamy composite, cinematic",
        "negative_prompt": "single flat layer, lowres, watermark",
    },
    {
        "name": "Glitch — Datamosh",
        "prompt": "glitch datamosh style {prompt}, RGB splits, compression artifacts, distorted geometry, surreal digital decay",
        "negative_prompt": "clean, lowres, watermark, text",
    },
    {
        "name": "Holographic — Iridescent",
        "prompt": "holographic iridescent rendering of {prompt}, metallic rainbow sheen, specular highlights, futuristic materials",
        "negative_prompt": "matte, lowres, watermark, text",
    },
    {
        "name": "Bioluminescent Night",
        "prompt": "bioluminescent night scene with {prompt}, glowing fungi and plants, soft ambient light, otherworldly atmosphere",
        "negative_prompt": "daylight, lowres, watermark, text",
    },
    {
        "name": "Hand-Drawn Chalkboard",
        "prompt": "hand-drawn chalkboard illustration of {prompt}, rough chalk textures, decorative flourishes, playful layout",
        "negative_prompt": "photorealistic, lowres, watermark",
    },
    {
        "name": "Ink & Water — Sumi-e",
        "prompt": "sumi-e ink wash painting {prompt}, expressive brush strokes, minimal composition, elegant negative space",
        "negative_prompt": "detailed texture, color, lowres, watermark",
    },
    {
        "name": "Futuristic UI — HUD",
        "prompt": "futuristic HUD interface showing {prompt}, translucent panels, neon accents, schematic lines, high-tech aesthetic",
        "negative_prompt": "analogue, lowres, watermark",
    },
    {
        "name": "Concept Sketch — Gesture",
        "prompt": "loose concept gesture sketch of {prompt}, quick lines, dynamic motion, creative ideation, raw pencil texture",
        "negative_prompt": "polished, lowres, watercolor",
    },
    {
        "name": "Photographic — Motion Portrait",
        "prompt": "motion blurred portrait of {prompt}, slow shutter panning, dynamic streaks, artistic long exposure portrait",
        "negative_prompt": "fully sharp, lowres, watermark",
    },
    {
        "name": "Landscape Painting — Tonal",
        "prompt": "tonal landscape painting of {prompt}, limited palette, atmospheric depth, subtle value gradations, evocative mood",
        "negative_prompt": "high saturation, lowres, watermark",
    },
    {
        "name": "Retro Futurism — Jetsons",
        "prompt": "retro futurism {prompt}, smooth rounded shapes, pastel palette, optimistic technology, mid-century vibe",
        "negative_prompt": "gritty, realistic, lowres, watermark",
    },
    {
        "name": "Neo-Expressionism",
        "prompt": "neo-expressionist canvas of {prompt}, raw paint gestures, intense colors, emotional distortion",
        "negative_prompt": "photorealistic, lowres, watermark",
    },
    {
        "name": "Social Documentary",
        "prompt": "documentary style photograph of {prompt}, candid moment, natural light, honest gritty texture, news magazine feel",
        "negative_prompt": "staged, lowres, watercolor, watermark",
    },
    {
        "name": "HDR Interior",
        "prompt": "high dynamic range interior shot featuring {prompt}, balanced exposures, soft window light, architectural detail",
        "negative_prompt": "flat exposure, lowres, sketch, watermark",
    },
    {
        "name": "Architectural — Minimal Contemporary",
        "prompt": "minimal contemporary architecture photo of {prompt}, clean lines, neutral palette, elegant negative space",
        "negative_prompt": "ornate, cluttered, lowres, watercolor",
    },
    {
        "name": "Conceptual — Metaphoric",
        "prompt": "conceptual metaphor image for {prompt}, symbolic elements, clean composition, editorial mood",
        "negative_prompt": "literal depiction, lowres, watermark",
    },
    {
        "name": "Bauhaus Graphic",
        "prompt": "bauhaus inspired graphic composition for {prompt}, primary colors, geometric balance, functional typography hint",
        "negative_prompt": "photorealistic, lowres, watercolor",
    },
    {
        "name": "Neo-Noir — Rainy Night",
        "prompt": "neo-noir rainy night scene with {prompt}, neon reflections, wet streets, moody backlight, cinematic grain",
        "negative_prompt": "bright daylight, lowres, cartoon",
    },
    {
        "name": "Polished Matte Illustration",
        "prompt": "polished matte illustration of {prompt}, soft lighting, muted color palette, editorial sophistication",
        "negative_prompt": "glossy, photorealistic, lowres, watermark",
    },
    {
        "name": "3D — Clay Render",
        "prompt": "clay render 3D model of {prompt}, neutral material, sculptural lighting, studio setup, concept model look",
        "negative_prompt": "textured PBR, high poly detail, lowres",
    },
    {
        "name": "3D — Toy Photography",
        "prompt": "toy photography style of {prompt}, small-scale props, shallow DOF, playful composition, vibrant colors",
        "negative_prompt": "life-size realism, lowres, watercolor",
    },
    {
        "name": "Monochrome Etching",
        "prompt": "etching style print of {prompt}, fine line detail, high contrast, antique print finish",
        "negative_prompt": "color, lowres, watercolor",
    },
    {
        "name": "Cinematic Color Grade — Teal & Orange",
        "prompt": "cinematic teal and orange color grade for {prompt}, warm highlights and cool shadows, filmic contrast",
        "negative_prompt": "flat color, lowres, watercolor",
    },
    {
        "name": "Fairy Tale — Storybook",
        "prompt": "storybook fairy tale illustration of {prompt}, soft textures, ornate borders, whimsical characters, cozy palette",
        "negative_prompt": "modern, lowres, watermark",
    },
    {
        "name": "Architectural Sketch — Isometric",
        "prompt": "isometric architectural sketch of {prompt}, precise linework, blueprint hints, minimal shading",
        "negative_prompt": "painterly, lowres, watermark",
    },
    {
        "name": "Surreal Portrait — Face Merge",
        "prompt": "surreal portrait merging elements around {prompt}, imaginative composite, uncanny but elegant",
        "negative_prompt": "plain portrait, lowres, watermark",
    },
    {
        "name": "Silk Screen Poster",
        "prompt": "silk screen poster design of {prompt}, limited palette, bold halftone, striking typography suggestion",
        "negative_prompt": "photorealistic, lowres, watercolor",
    },
    {
        "name": "Baroque Interior — Ornament",
        "prompt": "opulent baroque interior scene with {prompt}, gilded details, decorative molding, rich textiles",
        "negative_prompt": "minimal, lowres, watercolor",
    },
    {
        "name": "Neo-Classical Sculpture",
        "prompt": "neo-classical marble sculpture of {prompt}, elegant anatomy, soft diffused museum lighting, stone detail",
        "negative_prompt": "modern, lowres, cartoon",
    },
    {
        "name": "Digital Collage — Retro Ads",
        "prompt": "digital collage inspired by retro advertisements for {prompt}, vintage textures, product-focused layout, playful copy space",
        "negative_prompt": "photorealistic, lowres, watermark",
    },
    {
        "name": "Cinematic Close-Up — Macro Eye",
        "prompt": "cinematic macro close-up of {prompt}, extreme detail, eyelashes and texture, tear reflection, dramatic lighting",
        "negative_prompt": "wide shot, lowres, cartoon",
    },
    {
        "name": "Vaporwave — Pastel Dream",
        "prompt": "vaporwave pastel dream featuring {prompt}, retro computer motifs, marble statues, neon gradients, nostalgic haze",
        "negative_prompt": "realistic, lowres, watermark",
    },
    {
        "name": "Anatomical Illustration — Scientific",
        "prompt": "scientific anatomical illustration of {prompt}, precise labels, cross-section style, clean linework, educational clarity",
        "negative_prompt": "stylized, lowres, cartoon",
    },
    {
        "name": "Ethereal — Soft Glow",
        "prompt": "ethereal soft glow portrait of {prompt}, gentle bloom, pastel highlights, otherworldly ambiance",
        "negative_prompt": "harsh studio light, lowres, watermark",
    },
    {
        "name": "Fauvist Color Study",
        "prompt": "fauvist color study of {prompt}, wild saturated hues, loose brushwork, expressive palette",
        "negative_prompt": "photorealistic, lowres, watermark",
    },
    {
        "name": "Cutout Silhouette — Poster",
        "prompt": "cutout silhouette poster of {prompt}, strong shapes, high contrast, bold color background",
        "negative_prompt": "intricate texture, lowres, watermark",
    },
    {
        "name": "Neon Portrait — Rim Light",
        "prompt": "neon rim-lit portrait of {prompt}, vivid colored edges, moody contrast, cinematic close-up",
        "negative_prompt": "flat lighting, lowres, watermark",
    },
    {
        "name": "Silk Fabric Texture",
        "prompt": "luxurious silk fabric texture draped around {prompt}, soft highlights, smooth folds, tactile detail",
        "negative_prompt": "rough, lowres, watermark",
    },
    {
        "name": "Storyboard Frame",
        "prompt": "cinematic storyboard frame for {prompt}, clear action composition, thumbnail camera notes, readable silhouettes",
        "negative_prompt": "finished illustration, lowres, watermark",
    },
    {
        "name": "Architectural Render — White Model",
        "prompt": "white study architectural render of {prompt}, massing model, soft studio lighting, conceptual clarity",
        "negative_prompt": "textured materials, lowres, watercolor",
    },
    {
        "name": "Retro Comic — Silver Age",
        "prompt": "silver age comic book art of {prompt}, bold linework, flat colors, heroic composition, classic inks",
        "negative_prompt": "photorealistic, lowres, watercolor",
    },
    {
        "name": "Fine Art Photo — Platinum Print",
        "prompt": "fine art platinum print style photograph of {prompt}, high tonal range, velvety blacks, museum print quality",
        "negative_prompt": "vivid color, lowres, watermark",
    },
    {
        "name": "Cinematic Drone — Golden Landscape",
        "prompt": "cinematic drone golden hour landscape showing {prompt}, sweeping camera move, epic scale, high dynamic range",
        "negative_prompt": "tight crop, lowres, cartoon",
    },
    {
        "name": "Abstract Geometric Art",
        "prompt": "abstract geometric composition inspired by {prompt}, clean vector forms, spatial balance, minimal color scheme",
        "negative_prompt": "photorealistic, lowres, watermark",
    },
    {
        "name": "Pencil Portrait — Charcoal",
        "prompt": "pencil and charcoal portrait of {prompt}, rich charcoal shadows, refined graphite detail, textured paper",
        "negative_prompt": "color, lowres, watercolor",
    },
    {
        "name": "Surreal Landscape — Floating Islands",
        "prompt": "surreal floating islands landscape with {prompt}, vivid detail, impossible architecture, atmospheric depth",
        "negative_prompt": "mundane, lowres, watermark",
    },
    {
        "name": "Neo-Primitive Illustration",
        "prompt": "neo-primitive illustrative take on {prompt}, raw handmade marks, simple shapes, earthy palette",
        "negative_prompt": "polished digital, lowres, watercolor",
    },
    {
        "name": "Cinematic POV — First Person",
        "prompt": "first-person cinematic POV shot of {prompt}, immersive framing, depth, motion suggestions, high detail",
        "negative_prompt": "third-person distant, lowres, watermark",
    },
    {
        "name": "Monet-Style Impression",
        "prompt": "monet-inspired impressionist scene of {prompt}, soft broken color, shimmering surfaces, painterly touch",
        "negative_prompt": "photorealistic, lowres, watermark",
    },
    {
        "name": "Dramatic Spotlight — Theater",
        "prompt": "theatrical spotlight portrait of {prompt}, strong stage light, dark surrounding, high drama",
        "negative_prompt": "soft ambient lighting, lowres, watermark",
    },
    {
        "name": "Pop Surrealism",
        "prompt": "pop surrealist illustration of {prompt}, uncanny playful elements, bright palette, crisp linework",
        "negative_prompt": "documentary realism, lowres, watermark",
    },
    {
        "name": "Sculptural Clay Study",
        "prompt": "clay study sculpture render of {prompt}, visible tool marks, soft diffuse light, tactile volume",
        "negative_prompt": "polished marble, lowres, watercolor",
    },
    {
        "name": "High Key Fashion",
        "prompt": "high key fashion portrait of {prompt}, almost white background, airy feel, soft highlights, elegant styling",
        "negative_prompt": "moody low key, lowres, watermark",
    },
    {
        "name": "Low Key Moody",
        "prompt": "low key moody portrait of {prompt}, deep shadows, single rim light, intimate atmosphere",
        "negative_prompt": "bright, high key, lowres, watermark",
    },
    {
        "name": "Studio Still Life — Dutch Golden Age",
        "prompt": "still life in the style of dutch golden age for {prompt}, dramatic chiaroscuro, rich textures, meticulous detail",
        "negative_prompt": "minimal, modern, lowres, cartoon",
    },
    {
        "name": "Mixed Reality Composite",
        "prompt": "mixed reality composite of {prompt}, seamless photobashing and 3D elements, believable integration, cinematic finish",
        "negative_prompt": "naive collage, lowres, watermark",
    },
    {
        "name": "Cinematic Wide Angle — Environmental",
        "prompt": "wide angle cinematic environmental shot of {prompt}, expansive foreground, layered depth, dramatic sky",
        "negative_prompt": "tight portrait, lowres, watercolor",
    },
    {
        "name": "Retro Photograph — Kodachrome",
        "prompt": "kodachrome retro photograph of {prompt}, saturated warm tones, slight film grain, vintage feel",
        "negative_prompt": "modern digital, lowres, watermark",
    },
    {
        "name": "Architectural — Photogrammetry Realism",
        "prompt": "photogrammetry realistic capture of {prompt}, scanned texture detail, accurate scale, material realism",
        "negative_prompt": "painterly, lowres, watermark",
    },
    {
        "name": "Illustration — Flat Color Mid Century",
        "prompt": "mid-century flat color illustration of {prompt}, warm retro palette, simple shapes, editorial layout",
        "negative_prompt": "photorealistic, lowres, watermark",
    },
    {
        "name": "Brush Stroke Digital — Painterly",
        "prompt": "painterly digital brush stroke rendering of {prompt}, visible brush textures, layered paint feel, expressive",
        "negative_prompt": "photorealistic, lowres, watermark",
    },
    {
        "name": "Hyperreal Still Life",
        "prompt": "hyperreal still life of {prompt}, microsurface detail, perfect studio lighting, ultra high resolution",
        "negative_prompt": "sketchy, lowres, watercolor, cartoon",
    },
    {
        "name": "Atmospheric Fog — Moody",
        "prompt": "moody fog-laden scene of {prompt}, soft atmospheric depth, muted palette, cinematic mystery",
        "negative_prompt": "clear bright, lowres, watermark",
    },
    {
        "name": "Retro Illustration — Children Poster",
        "prompt": "vintage children poster illustration of {prompt}, wholesome color palette, bold shapes, toy-like charm",
        "negative_prompt": "gritty realism, lowres, watermark",
    },
    {
        "name": "Neo-Tech Blueprint",
        "prompt": "neo-tech schematic blueprint of {prompt}, wireframe overlays, technical annotations, futuristic engineering vibe",
        "negative_prompt": "organic, painterly, lowres, watermark",
    },
    {
        "name": "Mosaic — Byzantine Tile",
        "prompt": "byzantine mosaic tile style of {prompt}, tessellated gold and colored glass, religious iconography hint, intricate pattern",
        "negative_prompt": "smooth painting, lowres, watermark",
    },
    {
        "name": "Renaissance Fresco",
        "prompt": "renaissance fresco depiction of {prompt}, plaster texture, fresco pigments, soft classical lighting, historical realism",
        "negative_prompt": "modern, lowres, cartoon",
    },
    {
        "name": "Cinematic — Slow Motion Splash",
        "prompt": "ultra slow motion splash capture of {prompt}, droplets frozen, crystalline detail, backlit shimmer",
        "negative_prompt": "static, lowres, watercolor",
    },
    {
        "name": "Claymation Stop Motion",
        "prompt": "claymation stop-motion look for {prompt}, handmade texture, armature joints subtle, nostalgic craft feel",
        "negative_prompt": "CGI perfect, lowres, watercolor",
    },
    {
        "name": "Embossed Letterpress",
        "prompt": "embossed letterpress print of {prompt}, tactile impression, paper fiber detail, refined typographic hint",
        "negative_prompt": "flat digital, lowres, watermark",
    },
    {
        "name": "Handmade Textile Weave",
        "prompt": "handmade textile weave pattern featuring {prompt}, visible fibers, dyed threads, artisanal irregularities",
        "negative_prompt": "smooth digital, lowres, watercolor",
    },
    {
        "name": "Dream Pop — Pastel Clouds",
        "prompt": "dream pop skies of pastel clouds surrounding {prompt}, soft gradient, ethereal atmosphere, cotton candy tones",
        "negative_prompt": "dark, high contrast, lowres, watermark, text",
    },
    {
        "name": "Retro VHS — Glitchy Nostalgia",
        "prompt": "retro VHS footage of {prompt}, analog scanlines, chromatic aberration, timestamp overlay, grainy, warm tint",
        "negative_prompt": "clean digital, high resolution, modern, watermark",
    },
    {
        "name": "Noir Comic — Stylized Panels",
        "prompt": "noir comic panels of {prompt}, black and white with heavy contrast, speech bubble suggestion, gritty texture",
        "negative_prompt": "color, photorealistic, soft tones, low detail",
    },
    {
        "name": "Neon Flux — Vapor City",
        "prompt": "neon flux cyber city around {prompt}, reflective surfaces, glowing signs, dense urban, dynamic composition",
        "negative_prompt": "subdued tones, lowres, bland, watermark",
    },
    {
        "name": "Chalk Pastel — Soft Portrait",
        "prompt": "chalk pastel portrait of {prompt}, soft chalk edges, layered pastel pigments, elegant sketchy feel",
        "negative_prompt": "vector, crisp lines, digital flat, lowres",
    },
    {
        "name": "Infrared Landscape — Alien Flora",
        "prompt": "infrared style surreal landscape of {prompt}, glowing foliage, otherworldly colors, eerie yet beautiful",
        "negative_prompt": "realistic green, lowres, watermark",
    },
    {
        "name": "High Contrast Silkscreen",
        "prompt": "high contrast silkscreen print of {prompt}, limited color palette, bold blocks, graphic poster style",
        "negative_prompt": "gradation, texture, lowres, watermark",
    },
    {
        "name": "Soft Focus Bokeh Glow",
        "prompt": "soft focus glow around {prompt}, dreamy bokeh lights, pastel highlights, romantic cinematic blur",
        "negative_prompt": "sharp, high detail, harsh light, lowres",
    },
    {
        "name": "Lomo Effect — Vignette",
        "prompt": "Lomography-style shot of {prompt}, strong vignette, saturated colors, quirky framing, retro lens distortion",
        "negative_prompt": "flat color, high precision, lowres, watermark",
    },
    {
        "name": "Surreal Double Horizon",
        "prompt": "surreal scene with double horizon framing {prompt}, mirrored landscape, uncanny geometry, dreamlike",
        "negative_prompt": "normal landscape, lowres, watermark",
    },
    {
        "name": "Dynamic Feather Brush",
        "prompt": "dynamic feather brush strokes around {prompt}, expressive painterly marks, flowing energy, vibrant",
        "negative_prompt": "uniform fill, rigid lines, lowres, watermark",
    },
    {
        "name": "Frosted Glass Blur",
        "prompt": "frosted glass effect over {prompt}, soft diffused blur, translucent, abstract, dreamy layers",
        "negative_prompt": "sharp focus, clear details, lowres",
    },
    {
        "name": "Comic Halftone Color Splash",
        "prompt": "comic-style halftone with color splash highlighting {prompt}, dotted shading, bold color accent",
        "negative_prompt": "photorealistic, gradient, flat, lowres",
    },
    {
        "name": "Horror — Grainy Film Still",
        "prompt": "grainy horror film still of {prompt}, muted colors, harsh shadows, unsettling atmosphere",
        "negative_prompt": "bright, cheerful, lowres, cartoon, watermark",
    },
    {
        "name": "Bioluminescent Portrait",
        "prompt": "portrait lit by bioluminescent light emerging from {prompt}, glowing veins, soft blue-green light, mysterious",
        "negative_prompt": "daylight, lowres, flat",
    },
    {
        "name": "Architectural Blueprint Noir",
        "prompt": "noir-style architectural blueprint of {prompt}, white lines on black, dramatic shadows, grid background",
        "negative_prompt": "colored, painterly, lowres, watermark",
    },
    {
        "name": "Chiaroscuro Sketch",
        "prompt": "chiaroscuro pencil sketch of {prompt}, deep shadows and highlights, dramatic light contrast, artistic draft",
        "negative_prompt": "color, flat, lowres, watermark",
    },
    {
        "name": "Psychedelic Swirl",
        "prompt": "psychedelic swirl pattern behind {prompt}, vibrant swirling colors, trippy energy, retro 60s vibe",
        "negative_prompt": "muted, static, lowres, watermark",
    },
    {
        "name": "Old Storybook Etching",
        "prompt": "vintage storybook etching of {prompt}, fine crosshatch lines, antique paper look, narrative framing",
        "negative_prompt": "modern, color, lowres, watermark",
    },
    {
        "name": "Digital Noise Glitch",
        "prompt": "digital noise glitch overlaid on {prompt}, pixel distortions, static interference, cyber chaos aesthetic",
        "negative_prompt": "clean render, highres, low noise",
    },
    {
        "name": "Watercolor",
        "prompt": "Watercolor style illustration, delicate washes, soft edges, paper texture, hand-painted brushwork, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Gouache",
        "prompt": "Gouache style illustration, delicate washes, soft edges, paper texture, hand-painted brushwork, opaque layered color, matte finish, painterly strokes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Oil Painting",
        "prompt": "Oil Painting style illustration, visible brushstrokes, painterly texture, layered impasto, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Acrylic Painting",
        "prompt": "Acrylic Painting style illustration, visible brushstrokes, painterly texture, layered impasto, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Ink Wash (Sumi-e)",
        "prompt": "Ink Wash (Sumi-e) style illustration, delicate washes, soft edges, paper texture, hand-painted brushwork, high-contrast ink lines, crisp silhouettes, strong graphic linework, clean strokes, confident linework, expressive marks, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Pen and Ink",
        "prompt": "Pen and Ink style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, clean strokes, confident linework, expressive marks, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Charcoal Drawing",
        "prompt": "Charcoal Drawing style illustration, sketchy linework, hatching, paper grain, rough texture, hand-drawn feel, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Graphite Sketch",
        "prompt": "Graphite Sketch style illustration, sketchy linework, hatching, paper grain, rough texture, hand-drawn feel, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Pencil Sketch 2",
        "prompt": "Pencil Sketch style illustration, sketchy linework, hatching, paper grain, rough texture, hand-drawn feel, clean strokes, confident linework, expressive marks, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Colored Pencil",
        "prompt": "Colored Pencil style illustration, sketchy linework, hatching, paper grain, rough texture, hand-drawn feel, clean strokes, confident linework, expressive marks, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Pastel Portrait",
        "prompt": "Pastel Portrait style illustration, delicate washes, soft edges, paper texture, hand-painted brushwork, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Chalk Illustration",
        "prompt": "Chalk Illustration style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Marker Illustration",
        "prompt": "Marker Illustration style illustration, clean strokes, confident linework, expressive marks, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Crayon Illustration",
        "prompt": "Crayon Illustration style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Tempera Painting",
        "prompt": "Tempera Painting style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Fresco Style",
        "prompt": "Fresco Style style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Encaustic Texture",
        "prompt": "Encaustic Texture style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Spray Paint Street Art",
        "prompt": "Spray Paint Street Art style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Graffiti Stencil",
        "prompt": "Graffiti Stencil style illustration, torn paper textures, layered collage, photocopy distress, tactile cutouts, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Collage Mixed Media",
        "prompt": "Collage Mixed Media style illustration, torn paper textures, layered collage, photocopy distress, tactile cutouts, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Paper Cutout",
        "prompt": "Paper Cutout style illustration, torn paper textures, layered collage, photocopy distress, tactile cutouts, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Photomontage Collage",
        "prompt": "Photomontage Collage style illustration, torn paper textures, layered collage, photocopy distress, tactile cutouts, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Mosaic Tile",
        "prompt": "Mosaic Tile style illustration, tessellated forms, stitched textures, woven threads, tactile surface, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Stained Glass 2",
        "prompt": "Stained Glass style illustration, tessellated forms, stitched textures, woven threads, tactile surface, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Tapestry Weave",
        "prompt": "Tapestry Weave style illustration, tessellated forms, stitched textures, woven threads, tactile surface, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Embroidery Textile",
        "prompt": "Embroidery Textile style illustration, tessellated forms, stitched textures, woven threads, tactile surface, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Woodcut Print",
        "prompt": "Woodcut Print style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Linocut Print",
        "prompt": "Linocut Print style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Etching Engraving",
        "prompt": "Etching Engraving style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Lithograph Poster",
        "prompt": "Lithograph Poster style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Screenprint Silkscreen",
        "prompt": "Screenprint Silkscreen style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Halftone Pop Art",
        "prompt": "Halftone Pop Art style illustration, inked panels, halftone texture, dynamic poses, bold outlines, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Comic Book Ink",
        "prompt": "Comic Book Ink style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, clean strokes, confident linework, expressive marks, inked panels, halftone texture, dynamic poses, bold outlines, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Retro Comic Halftone",
        "prompt": "Retro Comic Halftone style illustration, inked panels, halftone texture, dynamic poses, bold outlines, neon gradients, retro color palette, glitch artifacts, nostalgic vibes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Vintage Poster Art Deco",
        "prompt": "Vintage Poster Art Deco style illustration, ornamental motifs, geometric patterns, decorative borders, stylized forms, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Pop Art High Contrast",
        "prompt": "Pop Art High Contrast style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Manga Style",
        "prompt": "Manga Style style illustration, inked panels, halftone texture, dynamic poses, bold outlines, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Anime Cel",
        "prompt": "Anime Cel style illustration, inked panels, halftone texture, dynamic poses, bold outlines, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Chibi Cartoon",
        "prompt": "Chibi Cartoon style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Cartoon Caricature",
        "prompt": "Cartoon Caricature style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Children's Book Illustration",
        "prompt": "Children's Book Illustration style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Storybook Watercolor",
        "prompt": "Storybook Watercolor style illustration, delicate washes, soft edges, paper texture, hand-painted brushwork, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Fantasy Illustration",
        "prompt": "Fantasy Illustration style illustration, dreamlike juxtapositions, uncanny elements, imaginative composition, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Concept Art Sketch",
        "prompt": "Concept Art Sketch style illustration, sketchy linework, hatching, paper grain, rough texture, hand-drawn feel, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Matte Painting Stylized",
        "prompt": "Matte Painting Stylized style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Digital Painting Brushwork",
        "prompt": "Digital Painting Brushwork style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Pixel Art 16-bit",
        "prompt": "Pixel Art 16-bit style illustration, pixel-perfect shapes, limited palette, retro videogame look, crisp pixels, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Pixel Art 8-bit",
        "prompt": "Pixel Art 8-bit style illustration, pixel-perfect shapes, limited palette, retro videogame look, crisp pixels, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Low-Poly Stylized",
        "prompt": "Low-Poly Stylized style illustration, pixel-perfect shapes, limited palette, retro videogame look, crisp pixels, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Vector Flat Design",
        "prompt": "Vector Flat Design style illustration, clean vector shapes, flat color areas, crisp edges, minimalist composition, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Minimalist Vector",
        "prompt": "Minimalist Vector style illustration, clean vector shapes, flat color areas, crisp edges, minimalist composition, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Isometric Illustration",
        "prompt": "Isometric Illustration style illustration, clean vector shapes, flat color areas, crisp edges, minimalist composition, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Technical Blueprint",
        "prompt": "Technical Blueprint style illustration, clean vector shapes, flat color areas, crisp edges, minimalist composition, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Line Art Minimal",
        "prompt": "Line Art Minimal style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Single Line Drawing",
        "prompt": "Single Line Drawing style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Contour Linework",
        "prompt": "Contour Linework style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Crosshatch Engraving",
        "prompt": "Crosshatch Engraving style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, sketchy linework, hatching, paper grain, rough texture, hand-drawn feel, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Stippling Pointillism",
        "prompt": "Stippling Pointillism style illustration, sketchy linework, hatching, paper grain, rough texture, hand-drawn feel, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Pointillism 2",
        "prompt": "Pointillism style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Neo-Impressionist",
        "prompt": "Neo-Impressionist style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Impressionist Brushwork 2",
        "prompt": "Impressionist Brushwork style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Post-Impressionist",
        "prompt": "Post-Impressionist style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Expressionist Painting",
        "prompt": "Expressionist Painting style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Fauvist Palette",
        "prompt": "Fauvist Palette style illustration, visible brushstrokes, painterly texture, layered impasto, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Cubist Geometry",
        "prompt": "Cubist Geometry style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Surrealist Dreamscape",
        "prompt": "Surrealist Dreamscape style illustration, dreamlike juxtapositions, uncanny elements, imaginative composition, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Dada Collage",
        "prompt": "Dada Collage style illustration, torn paper textures, layered collage, photocopy distress, tactile cutouts, dreamlike juxtapositions, uncanny elements, imaginative composition, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Abstract Expressionism 2",
        "prompt": "Abstract Expressionism style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Geometric Abstraction",
        "prompt": "Geometric Abstraction style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Color Field Painting 2",
        "prompt": "Color Field Painting style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Minimalist Graphic",
        "prompt": "Minimalist Graphic style illustration, clean vector shapes, flat color areas, crisp edges, minimalist composition, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Maximalist Decorative",
        "prompt": "Maximalist Decorative style illustration, ornamental motifs, geometric patterns, decorative borders, stylized forms, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Art Nouveau Ornament",
        "prompt": "Art Nouveau Ornament style illustration, ornamental motifs, geometric patterns, decorative borders, stylized forms, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Art Deco Geometry",
        "prompt": "Art Deco Geometry style illustration, ornamental motifs, geometric patterns, decorative borders, stylized forms, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Bauhaus Modernist",
        "prompt": "Bauhaus Modernist style illustration, ornamental motifs, geometric patterns, decorative borders, stylized forms, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Constructivist Poster",
        "prompt": "Constructivist Poster style illustration, ornamental motifs, geometric patterns, decorative borders, stylized forms, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Brutalist Graphic",
        "prompt": "Brutalist Graphic style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Futurist Motion",
        "prompt": "Futurist Motion style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Retro Futurism 2",
        "prompt": "Retro Futurism style illustration, neon gradients, retro color palette, glitch artifacts, nostalgic vibes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Vaporwave Pastel",
        "prompt": "Vaporwave Pastel style illustration, delicate washes, soft edges, paper texture, hand-painted brushwork, neon gradients, retro color palette, glitch artifacts, nostalgic vibes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Synthwave Neon",
        "prompt": "Synthwave Neon style illustration, neon gradients, retro color palette, glitch artifacts, nostalgic vibes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Cyberpunk Neon",
        "prompt": "Cyberpunk Neon style illustration, neon gradients, retro color palette, glitch artifacts, nostalgic vibes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Neon Noir 2",
        "prompt": "Neon Noir style illustration, inked panels, halftone texture, dynamic poses, bold outlines, neon gradients, retro color palette, glitch artifacts, nostalgic vibes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Glitch Art",
        "prompt": "Glitch Art style illustration, neon gradients, retro color palette, glitch artifacts, nostalgic vibes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Datamosh Effect",
        "prompt": "Datamosh Effect style illustration, neon gradients, retro color palette, glitch artifacts, nostalgic vibes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "VHS Retro",
        "prompt": "VHS Retro style illustration, neon gradients, retro color palette, glitch artifacts, nostalgic vibes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "CRT TV Scanlines",
        "prompt": "CRT TV Scanlines style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Film Grain Collage",
        "prompt": "Film Grain Collage style illustration, torn paper textures, layered collage, photocopy distress, tactile cutouts, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Double Exposure Collage",
        "prompt": "Double Exposure Collage style illustration, torn paper textures, layered collage, photocopy distress, tactile cutouts, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Silhouette Illustration",
        "prompt": "Silhouette Illustration style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Shadow Puppetry",
        "prompt": "Shadow Puppetry style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Chalkboard Sketch",
        "prompt": "Chalkboard Sketch style illustration, sketchy linework, hatching, paper grain, rough texture, hand-drawn feel, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Paper Quilling 2",
        "prompt": "Paper Quilling style illustration, tessellated forms, stitched textures, woven threads, tactile surface, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Origami Paper Art",
        "prompt": "Origami Paper Art style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Paper Collage Cutout",
        "prompt": "Paper Collage Cutout style illustration, torn paper textures, layered collage, photocopy distress, tactile cutouts, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Cutout Animation Style",
        "prompt": "Cutout Animation Style style illustration, torn paper textures, layered collage, photocopy distress, tactile cutouts, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Stop Motion Claymation",
        "prompt": "Stop Motion Claymation style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Puppet Illustration",
        "prompt": "Puppet Illustration style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Textile Collage",
        "prompt": "Textile Collage style illustration, torn paper textures, layered collage, photocopy distress, tactile cutouts, tessellated forms, stitched textures, woven threads, tactile surface, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Mixed Media Gouache",
        "prompt": "Mixed Media Gouache style illustration, delicate washes, soft edges, paper texture, hand-painted brushwork, opaque layered color, matte finish, painterly strokes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Foil Stamping Gold Leaf",
        "prompt": "Foil Stamping Gold Leaf style illustration, visible brushstrokes, painterly texture, layered impasto, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Embossed Illustration",
        "prompt": "Embossed Illustration style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Engraved Linework",
        "prompt": "Engraved Linework style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Foil Ink Illustration",
        "prompt": "Foil Ink Illustration style illustration, visible brushstrokes, painterly texture, layered impasto, high-contrast ink lines, crisp silhouettes, strong graphic linework, clean strokes, confident linework, expressive marks, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Woodburning Pyrography",
        "prompt": "Woodburning Pyrography style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Scratchboard Etching",
        "prompt": "Scratchboard Etching style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Sumi-e Minimal Ink",
        "prompt": "Sumi-e Minimal Ink style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, clean strokes, confident linework, expressive marks, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Chinese Brush Painting",
        "prompt": "Chinese Brush Painting style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Ukiyo-e Woodblock",
        "prompt": "Ukiyo-e Woodblock style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Japanese Ink Cartoon",
        "prompt": "Japanese Ink Cartoon style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, clean strokes, confident linework, expressive marks, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Persian Miniature",
        "prompt": "Persian Miniature style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Mughal Miniature",
        "prompt": "Mughal Miniature style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Byzantine Icon",
        "prompt": "Byzantine Icon style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Medieval Illuminated Manuscript",
        "prompt": "Medieval Illuminated Manuscript style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Gothic Manuscript",
        "prompt": "Gothic Manuscript style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Baroque Ornamentation",
        "prompt": "Baroque Ornamentation style illustration, ornamental motifs, geometric patterns, decorative borders, stylized forms, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Rococo Decorative",
        "prompt": "Rococo Decorative style illustration, ornamental motifs, geometric patterns, decorative borders, stylized forms, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Romantic Painterly",
        "prompt": "Romantic Painterly style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Symbolist Mystic",
        "prompt": "Symbolist Mystic style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Surreal Collage",
        "prompt": "Surreal Collage style illustration, torn paper textures, layered collage, photocopy distress, tactile cutouts, dreamlike juxtapositions, uncanny elements, imaginative composition, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Fantasy Map Illustration",
        "prompt": "Fantasy Map Illustration style illustration, dreamlike juxtapositions, uncanny elements, imaginative composition, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Architectural Illustration",
        "prompt": "Architectural Illustration style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Botanical Illustration",
        "prompt": "Botanical Illustration style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Scientific Illustration",
        "prompt": "Scientific Illustration style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Anatomical Drawing",
        "prompt": "Anatomical Drawing style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Fashion Illustration",
        "prompt": "Fashion Illustration style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Editorial Sketch",
        "prompt": "Editorial Sketch style illustration, sketchy linework, hatching, paper grain, rough texture, hand-drawn feel, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Infographic Flat",
        "prompt": "Infographic Flat style illustration, clean vector shapes, flat color areas, crisp edges, minimalist composition, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Children's Puzzle Illustration",
        "prompt": "Children's Puzzle Illustration style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Zine Collage Punk",
        "prompt": "Zine Collage Punk style illustration, torn paper textures, layered collage, photocopy distress, tactile cutouts, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "DIY Xerox Punk",
        "prompt": "DIY Xerox Punk style illustration, torn paper textures, layered collage, photocopy distress, tactile cutouts, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Grunge Poster",
        "prompt": "Grunge Poster style illustration, torn paper textures, layered collage, photocopy distress, tactile cutouts, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Retro 80s Graphic",
        "prompt": "Retro 80s Graphic style illustration, neon gradients, retro color palette, glitch artifacts, nostalgic vibes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Retro 90s Y2K",
        "prompt": "Retro 90s Y2K style illustration, neon gradients, retro color palette, glitch artifacts, nostalgic vibes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Neon Gradient Illustration",
        "prompt": "Neon Gradient Illustration style illustration, neon gradients, retro color palette, glitch artifacts, nostalgic vibes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Liquid Ink Bloom",
        "prompt": "Liquid Ink Bloom style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, clean strokes, confident linework, expressive marks, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Watercolor Bleed",
        "prompt": "Watercolor Bleed style illustration, delicate washes, soft edges, paper texture, hand-painted brushwork, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Wet-on-wet Painterly",
        "prompt": "Wet-on-wet Painterly style illustration, delicate washes, soft edges, paper texture, hand-painted brushwork, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Drybrush Texture",
        "prompt": "Drybrush Texture style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Palette Knife Impasto",
        "prompt": "Palette Knife Impasto style illustration, visible brushstrokes, painterly texture, layered impasto, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Thick Brush Strokes",
        "prompt": "Thick Brush Strokes style illustration, visible brushstrokes, painterly texture, layered impasto, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Sgraffito Scratch Texture",
        "prompt": "Sgraffito Scratch Texture style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Monochrome Ink",
        "prompt": "Monochrome Ink style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, clean strokes, confident linework, expressive marks, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Two-tone Silkscreen",
        "prompt": "Two-tone Silkscreen style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Monochrome Woodcut",
        "prompt": "Monochrome Woodcut style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "High Contrast Silhouette",
        "prompt": "High Contrast Silhouette style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Decorative Border Illustration",
        "prompt": "Decorative Border Illustration style illustration, ornamental motifs, geometric patterns, decorative borders, stylized forms, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Ornamental Filigree",
        "prompt": "Ornamental Filigree style illustration, ornamental motifs, geometric patterns, decorative borders, stylized forms, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Stencil Poster Art",
        "prompt": "Stencil Poster Art style illustration, torn paper textures, layered collage, photocopy distress, tactile cutouts, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Cut Paper Shadow",
        "prompt": "Cut Paper Shadow style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Collage Photomontage",
        "prompt": "Collage Photomontage style illustration, torn paper textures, layered collage, photocopy distress, tactile cutouts, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Photocopy Distressed",
        "prompt": "Photocopy Distressed style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Negative Space Illustration",
        "prompt": "Negative Space Illustration style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Silkscreen Punk Poster",
        "prompt": "Silkscreen Punk Poster style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Retro Travel Poster",
        "prompt": "Retro Travel Poster style illustration, neon gradients, retro color palette, glitch artifacts, nostalgic vibes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Vintage Book Illustration",
        "prompt": "Vintage Book Illustration style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Illustrated Map",
        "prompt": "Illustrated Map style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Tattoo Flash Sheet",
        "prompt": "Tattoo Flash Sheet style illustration, clean strokes, confident linework, expressive marks, bold outlines, flash sheet layout, limited palette, graphic motifs, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Traditional Tattoo Neo-Traditional",
        "prompt": "Traditional Tattoo Neo-Traditional style illustration, clean strokes, confident linework, expressive marks, bold outlines, flash sheet layout, limited palette, graphic motifs, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Dotwork Tattoo",
        "prompt": "Dotwork Tattoo style illustration, clean strokes, confident linework, expressive marks, bold outlines, flash sheet layout, limited palette, graphic motifs, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Linework Tattoo",
        "prompt": "Linework Tattoo style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, clean strokes, confident linework, expressive marks, bold outlines, flash sheet layout, limited palette, graphic motifs, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Neo-Geo Pattern",
        "prompt": "Neo-Geo Pattern style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Op Art Optical",
        "prompt": "Op Art Optical style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Kinetic Typography Illustration",
        "prompt": "Kinetic Typography Illustration style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Infused Calligraphy",
        "prompt": "Infused Calligraphy style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Hand-lettered Script",
        "prompt": "Hand-lettered Script style illustration, clean strokes, confident linework, expressive marks, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Calligraphic Ink",
        "prompt": "Calligraphic Ink style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, clean strokes, confident linework, expressive marks, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Typographic Poster",
        "prompt": "Typographic Poster style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Retro Engraving Illustration",
        "prompt": "Retro Engraving Illustration style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, neon gradients, retro color palette, glitch artifacts, nostalgic vibes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Etching Map",
        "prompt": "Etching Map style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Copperplate Engraving",
        "prompt": "Copperplate Engraving style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Mezzotint Texture",
        "prompt": "Mezzotint Texture style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Aquatint Wash",
        "prompt": "Aquatint Wash style illustration, delicate washes, soft edges, paper texture, hand-painted brushwork, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Sumi-e Minimalist",
        "prompt": "Sumi-e Minimalist style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, clean vector shapes, flat color areas, crisp edges, minimalist composition, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Minimal Papercut",
        "prompt": "Minimal Papercut style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Stylized Silhouette",
        "prompt": "Stylized Silhouette style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Cartoon Vector Sticker",
        "prompt": "Cartoon Vector Sticker style illustration, clean vector shapes, flat color areas, crisp edges, minimalist composition, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Kawaii Pastel Illustration",
        "prompt": "Kawaii Pastel Illustration style illustration, delicate washes, soft edges, paper texture, hand-painted brushwork, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Pastel Goth",
        "prompt": "Pastel Goth style illustration, delicate washes, soft edges, paper texture, hand-painted brushwork, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Moody Gouache",
        "prompt": "Moody Gouache style illustration, delicate washes, soft edges, paper texture, hand-painted brushwork, opaque layered color, matte finish, painterly strokes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Dreamy Pastel Wash",
        "prompt": "Dreamy Pastel Wash style illustration, delicate washes, soft edges, paper texture, hand-painted brushwork, dreamlike juxtapositions, uncanny elements, imaginative composition, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Cinematic Matte Pastel",
        "prompt": "Cinematic Matte Pastel style illustration, delicate washes, soft edges, paper texture, hand-painted brushwork, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Chalk Pastel Smudge",
        "prompt": "Chalk Pastel Smudge style illustration, delicate washes, soft edges, paper texture, hand-painted brushwork, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Soft Pencil Portrait",
        "prompt": "Soft Pencil Portrait style illustration, sketchy linework, hatching, paper grain, rough texture, hand-drawn feel, clean strokes, confident linework, expressive marks, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Crosshatch Portrait",
        "prompt": "Crosshatch Portrait style illustration, sketchy linework, hatching, paper grain, rough texture, hand-drawn feel, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Retro Linework Portrait",
        "prompt": "Retro Linework Portrait style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, neon gradients, retro color palette, glitch artifacts, nostalgic vibes, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Stylized Character Sheet",
        "prompt": "Stylized Character Sheet style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "RPG Character Portrait",
        "prompt": "RPG Character Portrait style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Illustrated Story Panel",
        "prompt": "Illustrated Story Panel style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Graphic Novel Noir",
        "prompt": "Graphic Novel Noir style illustration, inked panels, halftone texture, dynamic poses, bold outlines, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Noir Ink Drama",
        "prompt": "Noir Ink Drama style illustration, high-contrast ink lines, crisp silhouettes, strong graphic linework, clean strokes, confident linework, expressive marks, inked panels, halftone texture, dynamic poses, bold outlines, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Neo-Noir Graphic",
        "prompt": "Neo-Noir Graphic style illustration, inked panels, halftone texture, dynamic poses, bold outlines, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Cel Shaded 3D Cartoon",
        "prompt": "Cel Shaded 3D Cartoon style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Toon Shading Sketch",
        "prompt": "Toon Shading Sketch style illustration, sketchy linework, hatching, paper grain, rough texture, hand-drawn feel, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Paper Toy Design",
        "prompt": "Paper Toy Design style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Folded Paper Diorama",
        "prompt": "Folded Paper Diorama style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Pop Surrealism 2",
        "prompt": "Pop Surrealism style illustration, dreamlike juxtapositions, uncanny elements, imaginative composition, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Lowbrow Art",
        "prompt": "Lowbrow Art style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Outsider Art Folk",
        "prompt": "Outsider Art Folk style illustration, stylized, hand-drawn, illustration-focused, expressive linework, {prompt}, detailed linework, strong composition",
        "negative_prompt": "photorealistic, 3d, render, lowres, low quality, text, watermark, blurry, deformed, mutated"
    },
    {
        "name": "Patchwork Gouache Smear",
        "prompt": "gouache smear, dreamlike lighting, patchwork reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Mythic Metallic Emboss",
        "prompt": "metallic emboss, cinematic depth of field, mythic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Baroque Felt Applique",
        "prompt": "felt applique, subtle film grain, baroque reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Prismatic Felt Applique",
        "prompt": "felt applique, soft watercolor bleeds, prismatic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Isometric Ancient Tapestry",
        "prompt": "ancient tapestry, strong silhouettes, isometric reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Synthwave Vector Linocut",
        "prompt": "vector linocut, handmade craft feel, synthwave reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Psychedelic Paper Origami",
        "prompt": "paper origami, dreamlike lighting, psychedelic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Toy Photomicrography",
        "prompt": "photomicrography, prismatic refractions, toy reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, worst quality:1.3), watermark, unnatural skin, overexposed, blur, motion artefacts"
    },
    {
        "name": "Psychedelic Folk Embroidery",
        "prompt": "folk embroidery, rusted metallic surfaces, psychedelic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Neon Seed Bead Mosaic",
        "prompt": "seed-bead mosaic, muted pastel palette, neon reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Bio-mech Ancient Tapestry",
        "prompt": "ancient tapestry, tilt-shift miniature illusion, bio-mech reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Mythic Charcoal Sketch",
        "prompt": "charcoal sketch, handmade craft feel, mythic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Noir Sumi E Ink Wash",
        "prompt": "sumi-e ink wash, soft watercolor bleeds, noir reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Origami Sumi E Ink Wash",
        "prompt": "sumi-e ink wash, paper-texture details, origami reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "LowPoly Surreal Collage",
        "prompt": "surreal collage, cracked porcelain finish, lowpoly reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Vaporwave Sugar Glass Diorama",
        "prompt": "sugar-glass diorama, detailed embroidery stitches, vaporwave reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Voxel Gouache Smear",
        "prompt": "gouache smear, vector sharpness, voxel reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Kaleidoscopic Stipple Engraving",
        "prompt": "stipple engraving, ornate filigree, kaleidoscopic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Patchwork Magic Realism Painting",
        "prompt": "magic realism painting, cross-hatched shading, patchwork reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Diorama Photomicrography",
        "prompt": "photomicrography, high contrast shadows, diorama reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, worst quality:1.3), watermark, unnatural skin, overexposed, blur, motion artefacts"
    },
    {
        "name": "Vaporwave Retro Comic Cover",
        "prompt": "retro comic cover, cinematic depth of field, vaporwave reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Surreal Vector Linocut",
        "prompt": "vector linocut, cinematic depth of field, surreal reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Bioluminescent Steampunk Machinery",
        "prompt": "steampunk machinery, rusted metallic surfaces, bioluminescent reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Linocut Drip Paint Action",
        "prompt": "drip-paint action, cross-hatched shading, linocut reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Brutalist Cyberpunk Cityscape",
        "prompt": "cyberpunk cityscape, paper-texture details, brutalist reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Retro-futurist Retro Comic Cover",
        "prompt": "retro comic cover, rusted metallic surfaces, retro-futurist reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Bio-mech Lacquered Miniature",
        "prompt": "lacquered miniature, high contrast shadows, bio-mech reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Vector Drip Paint Action",
        "prompt": "drip-paint action, muted pastel palette, vector reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Voxel Sugar Glass Diorama",
        "prompt": "sugar-glass diorama, double exposure overlay, voxel reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Brutalist Architectural Blueprint",
        "prompt": "architectural blueprint, vector sharpness, brutalist reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Mythic Drip Paint Action",
        "prompt": "drip-paint action, cinematic depth of field, mythic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Prismatic Kaleidoscope Fractal",
        "prompt": "kaleidoscope fractal, ultra-detailed textures, prismatic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Psychedelic Low Poly Diorama",
        "prompt": "low-poly diorama, surreal scale shifts, psychedelic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Embroidery Iridescent Foil",
        "prompt": "iridescent foil, high contrast shadows, embroidery reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Retro-futurist Typographic Poster",
        "prompt": "typographic poster, surreal scale shifts, retro-futurist reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Retro-futurist Psychedelic Poster",
        "prompt": "psychedelic poster, foil stamping effects, retro-futurist reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed" 
    },
    {
        "name": "Embroidery Psychedelic Poster",
        "prompt": "psychedelic poster, detailed embroidery stitches, embroidery reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Minimalist Neon Signage",
        "prompt": "neon signage, floating geometry, minimalist reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Dreamcore Felt Applique",
        "prompt": "felt applique, cracked porcelain finish, dreamcore reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Papercraft Miniature Diorama",
        "prompt": "miniature diorama, floating geometry, papercraft reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Comic Anatomical Illustration",
        "prompt": "anatomical illustration, soft watercolor bleeds, comic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Eldritch Gouache Smear",
        "prompt": "gouache smear, fractured reflections, eldritch reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Patchwork Pen And Ink Stipple",
        "prompt": "pen-and-ink stipple, ink wash gradients, patchwork reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Vector Isometric Illustration",
        "prompt": "isometric illustration, vector sharpness, vector reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Origami Surreal Collage",
        "prompt": "surreal collage, detailed embroidery stitches, origami reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Pixel Neon Signage",
        "prompt": "neon signage, intricate patterns, pixel reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Prismatic Sugar Glass Diorama",
        "prompt": "sugar-glass diorama, dramatic backlight, prismatic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Prismatic Marquetry Inlay",
        "prompt": "marquetry inlay, rusted metallic surfaces, prismatic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Anamorphic Datamosh Glitch",
        "prompt": "datamosh glitch, dramatic backlight, anamorphic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Surreal Ancient Tapestry",
        "prompt": "ancient tapestry, muted pastel palette, surreal reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Linocut Stained Glass",
        "prompt": "stained glass, cracked porcelain finish, linocut reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Comic Seed Bead Mosaic",
        "prompt": "seed-bead mosaic, neon gradient palette, comic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Comic Sumi E Ink Wash",
        "prompt": "sumi-e ink wash, ancient symbol motifs, comic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Patchwork Paper Origami",
        "prompt": "paper origami, limited color scheme, patchwork reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Minimalist Cyberpunk Cityscape",
        "prompt": "cyberpunk cityscape, muted pastel palette, minimalist reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Voxel Lego Mosaic",
        "prompt": "lego mosaic, intricate patterns, voxel reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, worst quality,), watermark, text, oversmoothing, muddy colors"
    },
    {
        "name": "Vector Kaleidoscope Fractal",
        "prompt": "kaleidoscope fractal, foil stamping effects, vector reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Synthwave Gouache Smear",
        "prompt": "gouache smear, cross-hatched shading, synthwave reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Magical Metallic Emboss",
        "prompt": "metallic emboss, ultra-detailed textures, magical reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Dreamcore Typographic Poster",
        "prompt": "typographic poster, soft watercolor bleeds, dreamcore reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Kaleidoscopic Sugar Glass Diorama",
        "prompt": "sugar-glass diorama, foil stamping effects, kaleidoscopic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Glitch Seed Bead Mosaic",
        "prompt": "seed-bead mosaic, floating geometry, glitch reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Baroque Retro Comic Cover",
        "prompt": "retro comic cover, woodgrain imperfections, baroque reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Toy Pen And Ink Stipple",
        "prompt": "pen-and-ink stipple, cracked porcelain finish, toy reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Pixel Surreal Collage",
        "prompt": "surreal collage, ink wash gradients, pixel reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Retro-futurist Marquetry Inlay",
        "prompt": "marquetry inlay, limited color scheme, retro-futurist reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Magical Bio Mech Anatomy",
        "prompt": "bio-mech anatomy, cross-hatched shading, magical reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Woodcut Lego Mosaic",
        "prompt": "lego mosaic, stippling texture, woodcut reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, worst quality,), watermark, text, oversmoothing, muddy colors"
    },
    {
        "name": "Gothic Metallic Emboss",
        "prompt": "metallic emboss, cinematic depth of field, gothic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Glitch Datamosh Glitch",
        "prompt": "datamosh glitch, dreamlike lighting, glitch reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Isometric Stipple Engraving",
        "prompt": "stipple engraving, cinematic depth of field, isometric reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Isometric Miniature Diorama",
        "prompt": "miniature diorama, intricate patterns, isometric reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Glitch Collagraph Print",
        "prompt": "collagraph print, ultra-detailed textures, glitch reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Psychedelic Isometric Illustration",
        "prompt": "isometric illustration, strong silhouettes, psychedelic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Noir Isometric Illustration",
        "prompt": "isometric illustration, double exposure overlay, noir reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Mythic Retro Comic Cover",
        "prompt": "retro comic cover, foil stamping effects, mythic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Diorama Typographic Poster",
        "prompt": "typographic poster, woodgrain imperfections, diorama reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Dreamcore Technical Cutaway",
        "prompt": "technical cutaway, prismatic refractions, dreamcore reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Dieselpunk Sumi E Ink Wash",
        "prompt": "sumi-e ink wash, subtle film grain, dieselpunk reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Holographic Ancient Tapestry",
        "prompt": "ancient tapestry, paper-texture details, holographic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Stained-Glass Cosmic Horror Tableau",
        "prompt": "cosmic horror tableau, detailed embroidery stitches, stained-glass reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Eldritch Lacquered Miniature",
        "prompt": "lacquered miniature, subtle film grain, eldritch reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Eldritch Bio Mech Anatomy",
        "prompt": "bio-mech anatomy, tilt-shift miniature illusion, eldritch reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Bioluminescent Metallic Emboss",
        "prompt": "metallic emboss, limited color scheme, bioluminescent reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Dieselpunk Marquetry Inlay",
        "prompt": "marquetry inlay, stippling texture, dieselpunk reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Baroque Ancient Tapestry",
        "prompt": "ancient tapestry, neon gradient palette, baroque reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Mythic Architectural Blueprint",
        "prompt": "architectural blueprint, double exposure overlay, mythic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Glitch Folk Embroidery",
        "prompt": "folk embroidery, subtle film grain, glitch reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Eldritch Psychedelic Poster",
        "prompt": "psychedelic poster, intricate patterns, eldritch reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Kaleidoscopic Seed Bead Mosaic",
        "prompt": "seed-bead mosaic, double exposure overlay, kaleidoscopic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Brutalist Cosmic Horror Tableau",
        "prompt": "cosmic horror tableau, foil stamping effects, brutalist reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Etching Toy Photography",
        "prompt": "toy-photography, glowing bioluminescence, etching reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, worst quality:1.3), watermark, unnatural skin, overexposed, blur, motion artefacts"
    },
    {
        "name": "Eldritch Pen And Ink Stipple",
        "prompt": "pen-and-ink stipple, vector sharpness, eldritch reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Neon Steampunk Machinery",
        "prompt": "steampunk machinery, cracked porcelain finish, neon reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Linocut Lenticular Poster",
        "prompt": "lenticular poster, ink wash gradients, linocut reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Bio-mech Sugar Glass Diorama",
        "prompt": "sugar-glass diorama, foil stamping effects, bio-mech reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Minimalist Photomicrography",
        "prompt": "photomicrography, ornate filigree, minimalist reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, worst quality:1.3), watermark, unnatural skin, overexposed, blur, motion artefacts"
    },
    {
        "name": "Retro-futurist 8 Bit Pixel Art",
        "prompt": "8-bit pixel art, ultra-detailed textures, retro-futurist reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, worst quality,), watermark, text, oversmoothing, muddy colors"
    },
    {
        "name": "Cinematic 8 Bit Pixel Art",
        "prompt": "8-bit pixel art, ultra-detailed textures, cinematic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, worst quality,), watermark, text, oversmoothing, muddy colors"
    },
    {
        "name": "Isometric Technical Cutaway",
        "prompt": "technical cutaway, muted pastel palette, isometric reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Eldritch Paper Origami",
        "prompt": "paper origami, soft watercolor bleeds, eldritch reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Steampunk Isometric Illustration",
        "prompt": "isometric illustration, high contrast shadows, steampunk reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Prismatic Metallic Emboss",
        "prompt": "metallic emboss, glowing bioluminescence, prismatic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Gothic Typographic Poster",
        "prompt": "typographic poster, double exposure overlay, gothic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Isometric Surreal Collage",
        "prompt": "surreal collage, strong silhouettes, isometric reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Collage Vector Linocut",
        "prompt": "vector linocut, prismatic refractions, collage reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Holographic Film Noir Frame",
        "prompt": "film noir frame, surreal scale shifts, holographic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Folkloric Toy Photography",
        "prompt": "toy-photography, surreal scale shifts, folkloric reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, worst quality:1.3), watermark, unnatural skin, overexposed, blur, motion artefacts"
    },
    {
        "name": "Dreamcore Neon Signage",
        "prompt": "neon signage, glowing bioluminescence, dreamcore reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Linocut Kaleidoscope Fractal",
        "prompt": "kaleidoscope fractal, high contrast shadows, linocut reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Neon Architectural Blueprint",
        "prompt": "architectural blueprint, subtle film grain, neon reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Glitch Marquetry Inlay",
        "prompt": "marquetry inlay, handmade craft feel, glitch reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Comic Neon Signage",
        "prompt": "neon signage, floating geometry, comic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "LowPoly Isometric Illustration",
        "prompt": "isometric illustration, double exposure overlay, lowpoly reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Papercraft Lenticular Poster",
        "prompt": "lenticular poster, muted pastel palette, papercraft reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Woodcut Marquetry Inlay",
        "prompt": "marquetry inlay, ancient symbol motifs, woodcut reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Collage Psychedelic Poster",
        "prompt": "psychedelic poster, intricate patterns, collage reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Holographic Stipple Engraving",
        "prompt": "stipple engraving, ancient symbol motifs, holographic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Holographic Sumi E Ink Wash",
        "prompt": "sumi-e ink wash, floating geometry, holographic reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Folkloric Gouache Smear",
        "prompt": "gouache smear, subtle film grain, folkloric reinterpretation of {prompt}, intricate composition, strong mood, cinematic framing, ultra-detailed, high resolution",
        "negative_prompt": "(lowres, low quality), watermark, text, signature, frame, blurry, deformed"
    },
    {
        "name": "Surreal Dreamscape",
        "prompt": "surreal dreamscape, floating architecture, impossible perspective, {prompt}, painterly, otherworldly details, symbolic imagery",
        "negative_prompt": "photorealistic, lowres, text, watermark, deformed, ugly, blurry",
    },
    {
        "name": "Cubist Collage",
        "prompt": "cubist collage treatment, fragmented planes, geometric abstraction, layered faces and objects, {prompt}, analytical cubism feel",
        "negative_prompt": "photo, photorealistic, soft focus, blurred, text, watermark",
    },
    {
        "name": "Psychedelic 60s Poster",
        "prompt": "psychedelic 1960s concert poster, swirling ornaments, bold type-like shapes, highly saturated gradients, {prompt}, trippy patterns",
        "negative_prompt": "muted colors, photorealistic, lowres, watermark, text",
    },
    {
        "name": "Vaporwave 2",
        "prompt": "vaporwave aesthetic, retro-futuristic, pastel neon gradients, Greek statue busts, VHS grain, {prompt}, dreamy nostalgia",
        "negative_prompt": "realistic, high detail photo, watermark, tilted horizon, ugly",
    },
    {
        "name": "Synthwave / Retrowave",
        "prompt": "synthwave retro 80s, neon grid, sun with chromatic glow, cinematic silhouette, {prompt}, high contrast neon",
        "negative_prompt": "photorealistic, muddy, lowres, text, watermark",
    },
    {
        "name": "Ukiyo-e Woodblock 2",
        "prompt": "ukiyo-e woodblock print style, flat areas of color, strong outlines, textured paper grain, {prompt}, traditional Japanese composition",
        "negative_prompt": "3d, photorealistic, modern lens effects, blurry, watermark",
    },
    {
        "name": "Gouache Illustration 2",
        "prompt": "gouache painting, opaque layered brushstrokes, soft edges, tactile paper texture, {prompt}, illustrative composition",
        "negative_prompt": "photo, realistic, muddy, noisy, watermark",
    },
    {
        "name": "Papercut Collage 2",
        "prompt": "papercut collage, crisp paper edges, layered cut shapes, drop shadows, handcrafted look, {prompt}, simplified color blocks",
        "negative_prompt": "photorealistic, grainy, blurred, watermark, text",
    },
    {
        "name": "Caricature Cartoon",
        "prompt": "exaggerated caricature, playful proportions, bold linework, expressive features, {prompt}, high personality",
        "negative_prompt": "realistic anatomy, photo, lowres, watermark, text",
    },
    {
        "name": "Low-Poly 3D",
        "prompt": "low-poly 3d style, faceted geometry, flat shading, stylized polygonal forms, {prompt}, clean silhouette",
        "negative_prompt": "photorealistic, high poly, detailed textures, noise, watermark",
    },
    {
        "name": "Pixel Art (16-bit)",
        "prompt": "pixel art 16-bit, limited palette, crisp pixels, isometric vibes optional, {prompt}, retro game sprite composition",
        "negative_prompt": "smooth gradients, photorealistic, blur, watermark",
    },
    {
        "name": "Isometric Game Art",
        "prompt": "isometric game art, tiny world, tile detail, charming miniatures, {prompt}, handcrafted game-sprite feel",
        "negative_prompt": "photo, 3d photorealistic, lowres, watermark",
    },
    {
        "name": "Flat Vector Art",
        "prompt": "flat vector illustration, simple shapes, bold negative space, clean edges, {prompt}, poster-ready composition",
        "negative_prompt": "photorealistic, texture, grain, blur, watermark",
    },
    {
        "name": "Papercraft Diorama",
        "prompt": "miniature papercraft diorama, layered depth, soft studio light, handcrafted paper textures, {prompt}, whimsical scale",
        "negative_prompt": "photo, photorealistic, noisy, watermark",
    },
    {
        "name": "Stained Glass 3",
        "prompt": "stained glass window style, leaded outlines, jewel-tone panes, luminous backlight, {prompt}, ornamental motifs",
        "negative_prompt": "photo, realistic faces, blur, watermark, text",
    },
    {
        "name": "Linocut / Woodcut",
        "prompt": "linocut print, high contrast relief carving marks, limited palette, bold contours, {prompt}, craft printmaking aesthetic",
        "negative_prompt": "photo, soft gradients, blur, watermark",
    },
    {
        "name": "Pointillism 2",
        "prompt": "pointillist stippling technique, tiny dots build color and light, {prompt}, painterly optical mixing",
        "negative_prompt": "photorealistic, blur, lowres, watermark",
    },
    {
        "name": "Op Art (Optical)",
        "prompt": "op-art optical patterning, moiré illusions, high-contrast geometric repeats, {prompt}, dizzying visual rhythm",
        "negative_prompt": "photo, soft edges, blur, watermark",
    },
    {
        "name": "Collage & Mixed Media",
        "prompt": "mixed media collage, torn paper, ink scribbles, photographed textures, {prompt}, layered eclectic composition",
        "negative_prompt": "clean photorealistic, lowres, watermark, text",
    },
    {
        "name": "Silkscreen / Pop Art",
        "prompt": "silkscreen pop-art halftone, bold shapes, limited high-contrast palette, {prompt}, graphic poster quality",
        "negative_prompt": "photo, realistic lighting, blur, watermark",
    },
    {
        "name": "Children's Book Whimsy",
        "prompt": "children's book illustration, soft playful characters, rounded shapes, gentle palette, {prompt}, storybook charm",
        "negative_prompt": "gory, realistic violence, photorealistic, watermark",
    },
    {
        "name": "Sticker / Emblem",
        "prompt": "sticker art, bold outline, simplified silhouette, badge composition, {prompt}, high readability at small sizes",
        "negative_prompt": "photo, noisy texture, blur, watermark",
    },
    {
        "name": "Cloth Embroidery Texture",
        "prompt": "embroidered textile look, stitched threads, fabric texture, tactile highlights and shadows, {prompt}, handcrafted embroidery style",
        "negative_prompt": "photo, realistic skin detail, blur, watermark",
    },
    {
        "name": "Hand-Drawn Comic Ink",
        "prompt": "inktober-style hand inked comic panel, expressive hatching and line weight, dynamic composition, {prompt}, sequential art energy",
        "negative_prompt": "photo, soft brush paint, blur, watermark",
    },
    {
        "name": "Retro Paper Poster",
        "prompt": "vintage paper poster, slightly faded inks, halftone aging, retro typography vibes, {prompt}, collectible poster look",
        "negative_prompt": "photo, modern glossy finish, watermark, text",
    },
    {
        "name": "Bauhaus Geometric",
        "prompt": "bauhaus inspired geometric composition, primary colors, functional simplicity, {prompt}, modernist graphic balance",
        "negative_prompt": "photo, ornate details, blur, watermark",
    },
    {
        "name": "Art Nouveau Flow",
        "prompt": "art nouveau ornamental flow, sinuous lines, floral motif framing, elegant figure composition, {prompt}, decorative organic forms",
        "negative_prompt": "photorealistic, harsh lighting, blur, watermark",
    },
    {
        "name": "Constructivist Poster 2",
        "prompt": "constructivist propaganda poster style, angular shapes, strong diagonals, typographic blocks, {prompt}, bold limited palette",
        "negative_prompt": "photo, soft edges, blur, watermark",
    },
    {
        "name": "Art Deco Glam",
        "prompt": "art deco ornamentation, geometric luxury, metallic accents, sleek silhouettes, {prompt}, 1920s glamour",
        "negative_prompt": "grunge, messy texture, photorealistic, blur, watermark",
    },
    {
        "name": "Steampunk Illustration",
        "prompt": "steampunk mechanical Victorian, brass gears, steam pipes, whimsical contraptions, {prompt}, intricate hand-drawn detail",
        "negative_prompt": "modern tech, photorealistic, blur, watermark",
    },
    {
        "name": "Dieselpunk Noir",
        "prompt": "dieselpunk gritty 1930s-40s, industrial silhouettes, smoky atmospherics, {prompt}, noir mood",
        "negative_prompt": "bright pop, photorealistic, watermark",
    },
    {
        "name": "Film Noir Graphic",
        "prompt": "film noir graphic, high-contrast chiaroscuro, dramatic silhouettes and smoke, {prompt}, cinematic 1940s vibe",
        "negative_prompt": "colorful, pastel, photorealistic, watermark",
    },
    {
        "name": "Kaleidoscope Symmetry",
        "prompt": "kaleidoscopic symmetry, mirrored fractal motifs, intricate repeating ornament, {prompt}, hypnotic pattern",
        "negative_prompt": "photo, asymmetry, blur, watermark",
    },
    {
        "name": "Collage Photo-Illustration",
        "prompt": "photo-illustration collage blend, cut-and-paste photos with painted overlays, {prompt}, surreal editorial look",
        "negative_prompt": "plain photo, raw jpeg artifacts, watermark, text",
    },
    {
        "name": "Claymation / Stop-Motion",
        "prompt": "stop-motion claymation style, tactile sculpted forms, visible fingerprints and seams, {prompt}, handcrafted animation look",
        "negative_prompt": "3d render, photorealistic, blur, watermark",
    },
    {
        "name": "Miniature Model (Toy-like)",
        "prompt": "toy model diorama aesthetic, painted miniature feel, shallow depth of field optional, {prompt}, playful scale",
        "negative_prompt": "real human faces, photorealistic, blur, watermark",
    },
    {
        "name": "Vector Flat UI",
        "prompt": "flat UI illustration, clean iconography, simplified forms, negative space, {prompt}, scalable vector look",
        "negative_prompt": "photo, texture, grime, blur, watermark",
    },
    {
        "name": "Zine / Xerox Punk",
        "prompt": "zine xerox punk aesthetic, high-contrast photocopy textures, hand-cut letters, collage grit, {prompt}, DIY raw energy",
        "negative_prompt": "polished, glossy, photorealistic, watermark",
    },
    {
        "name": "Stencil Graffiti",
        "prompt": "street-art stencil, spray paint edge, urban rough wall texture, bold silhouette, {prompt}, rebellious poster quality",
        "negative_prompt": "pristine studio photo, polished finish, watermark",
    },
    {
        "name": "Tattoo Flash Art",
        "prompt": "traditional tattoo flash sheet, bold outlines, limited palette, iconographic motifs, {prompt}, vintage flash layout",
        "negative_prompt": "photo, soft gradients, blur, watermark",
    },
    {
        "name": "Handmade Ceramic Glaze",
        "prompt": "hand-thrown ceramic texture, reactive glaze speckles, kiln-fired color shifts, {prompt}, tactile potters' finish",
        "negative_prompt": "flat digital, photorealistic metal, watermark",
    },
    {
        "name": "Fresco Mural",
        "prompt": "fresco mural texture, subtle plaster cracks, mineral pigments, classical composition, {prompt}, aged wall painting",
        "negative_prompt": "clean studio photo, glossy sheen, watermark",
    },
    {
        "name": "Charcoal Sketch",
        "prompt": "loose charcoal sketching, rich blacks and smudged greys, energetic marks, {prompt}, expressive figure drawing",
        "negative_prompt": "photo, color, blur, watermark",
    },
    {
        "name": "Ink Wash (Sumi-e) 2",
        "prompt": "sumi-e ink wash minimalism, wet brush gradients, bold calligraphic strokes, {prompt}, contemplative negative space",
        "negative_prompt": "photo, heavy texture, color, watermark",
    },
    {
        "name": "Watercolor Bleed 2",
        "prompt": "watercolor wet-into-wet bleed, translucent layers, paper granulation, {prompt}, delicate painterly wash",
        "negative_prompt": "sharp photographic detail, heavy noise, watermark",
    },
    {
        "name": "Sgraffito Scratch",
        "prompt": "sgraffito scratch technique, incised lines over color layers, tactile scrape marks, {prompt}, folk-art feel",
        "negative_prompt": "photo, glossy finish, blur, watermark",
    },
    {
        "name": "Mosaic Tile 2",
        "prompt": "tile mosaic assembly, tessellated colored pieces, grout lines visible, {prompt}, Byzantine decorative geometry",
        "negative_prompt": "photo, smooth gradients, blur, watermark",
    },
    {
        "name": "Neon Sign Typography",
        "prompt": "neon sign lettering, bent glass glow, subtle smoke, urban night storefront, {prompt}, retro signage vibe",
        "negative_prompt": "daylight photo, realistic person, blur, watermark",
    },
    {
        "name": "Kinetic Sculpture Diagram",
        "prompt": "kinetic sculpture blueprint style, mechanical diagrams, annotated moving parts, {prompt}, conceptual engineering art",
        "negative_prompt": "photorealistic render, soft painterly, blur, watermark",
    },
    {
        "name": "Cut-paper Silhouette",
        "prompt": "cut-paper silhouette portrait, single-color backdrop, delicate profile detail, {prompt}, shadow-play composition",
        "negative_prompt": "photo, color photo, blur, watermark",
    },
    {
        "name": "Stencil Pattern Repeat",
        "prompt": "seamless stencil repeat pattern, crisp edges, decorative motif, {prompt}, textile surface-ready",
        "negative_prompt": "photorealistic lighting, blur, watermark",
    },
    {
        "name": "Fossil / Etching",
        "prompt": "fine-line etching or fossil relief, minute engraved detail, monochrome tonal range, {prompt}, archival print feel",
        "negative_prompt": "photo, color, blur, watermark",
    },
    {
        "name": "Retro Comic Halftone 2",
        "prompt": "retro comic halftone dots, bold captions, dynamic paneling, {prompt}, vintage pulp energy",
        "negative_prompt": "smooth gradients, photorealistic, blur, watermark",
    },
    {
        "name": "Monochrome Silkscreen",
        "prompt": "single-color silkscreen print, strong graphic contrast, texture of ink edges, {prompt}, pop graphic statement",
        "negative_prompt": "photo, multicolor realism, blur, watermark",
    },
    {
        "name": "Sticker Sheet Collage",
        "prompt": "sticker sheet layout, different small icons and patches, playful variety, {prompt}, high-contrast outlines",
        "negative_prompt": "photo, low-contrast, blur, watermark",
    },
    {
        "name": "Doodle Sketchbook",
        "prompt": "loose doodle sketchbook page, playful icons, margin notes, {prompt}, spontaneous hand-drawn charm",
        "negative_prompt": "photorealistic, precise rendering, blur, watermark",
    },
    {
        "name": "Retro Futurism Illustration",
        "prompt": "retro-futurism, chrome curves, optimistic space-age design, {prompt}, vintage sci-fi poster",
        "negative_prompt": "gritty realism, modern meme elements, blur, watermark",
    },
    {
        "name": "Kawaii Chibi",
        "prompt": "kawaii chibi character design, oversized head, tiny body, huge eyes, {prompt}, sugary pastel palette",
        "negative_prompt": "realistic proportions, mature themes, gore, watermark",
    },
    {
        "name": "Manga Screentone",
        "prompt": "classic manga screentone texture, dynamic action lines, stylized anatomy, {prompt}, black-and-white graphic storytelling",
        "negative_prompt": "photo, color gradients, blur, watermark",
    },
    {
        "name": "Anime Cell Shading",
        "prompt": "anime cell-shaded style, crisp rim lighting, clean lineart, cinematic posing, {prompt}, bold color flats",
        "negative_prompt": "photorealistic, dirty texture, blur, watermark",
    },
    {
        "name": "Storyboard / Concept Sketch",
        "prompt": "tight storyboard thumbnail, clear silhouette language, composition focus, {prompt}, narrative beat",
        "negative_prompt": "photo, detailed texture, blur, watermark",
    },
    {
        "name": "Character Model Sheet",
        "prompt": "character model sheet layout, turnaround poses, expression sets, accessory callouts, {prompt}, clean orthographic views",
        "negative_prompt": "photorealistic finish, blur, watermark",
    },
    {
        "name": "Toyetic Vinyl Figure",
        "prompt": "designer vinyl toy concept, simplified forms, glossy plastic finish, collectible figure silhouette, {prompt}, playful proportions",
        "negative_prompt": "real human, gore, photorealistic, blur, watermark",
    },
    {
        "name": "Stencil Pop Portrait",
        "prompt": "pop-art stencil portrait, two-tone contrast, iconized face, {prompt}, street-friendly aesthetics",
        "negative_prompt": "detailed photo texture, blur, watermark",
    },
    {
        "name": "Sticker Minimal Logo",
        "prompt": "minimal logo / sticker concept, bold glyph, negative-space cleverness, {prompt}, scalable vector-friendly",
        "negative_prompt": "photo, complex shading, blur, watermark",
    },
    {
        "name": "Mandala Ornamental",
        "prompt": "intricate mandala radial symmetry, layered decorative flourishes, meditative patterning, {prompt}, ornamental balance",
        "negative_prompt": "photo, messy composition, blur, watermark",
    },
    {
        "name": "Anamorphic Illusion",
        "prompt": "anamorphic optical illusion perspective, distorted plane that reads from one viewpoint, {prompt}, playful trompe-l'oeil",
        "negative_prompt": "flat photo, blur, watermark",
    },
    {
        "name": "Retro Anime 90s",
        "prompt": "90s anime aesthetic, soft cell-shading, lens flares, cinematic framing, {prompt}, nostalgia-driven composition",
        "negative_prompt": "hyperrealism, modern photorealistic skin, watermark",
    },
    {
        "name": "Moebius / Ligne Claire Inspired",
        "prompt": "ligne claire clean line comic with intricate worldbuilding, airy linework, flat color fields, {prompt}, clear narrative detail",
        "negative_prompt": "photo, painterly texture, blur, watermark",
    },
    {
        "name": "Fantasy Map Illustration 2",
        "prompt": "ornamental fantasy map, labeled cartography elements, textured parchment, {prompt}, illustrated legend and compass",
        "negative_prompt": "photo, modern map satellite, blur, watermark",
    },
    {
        "name": "Alchemical Diagram",
        "prompt": "alchemical diagram aesthetic, symbolic glyphs, distressed vellum texture, {prompt}, occult schematic vibe",
        "negative_prompt": "photo, modern icons, blur, watermark",
    },
    {
        "name": "Blueprint / Tech Schematic",
        "prompt": "engineer's blueprint linework, annotated measurements, exploded views, {prompt}, schematic clarity",
        "negative_prompt": "photo, painterly, blur, watermark",
    },
    {
        "name": "Pulp Magazine Cover",
        "prompt": "pulp magazine cover styling, dramatic captioning, exaggerated action scene, {prompt}, retro pulp color palette",
        "negative_prompt": "clean modern photo, blur, watermark",
    },
    {
        "name": "Hand-painted Mural",
        "prompt": "hand-painted mural brushwork, scale-aware composition, visible brush marks, {prompt}, public art presence",
        "negative_prompt": "photo, studio finish, blur, watermark",
    },
    {
        "name": "Graffiti Wildstyle",
        "prompt": "graffiti wildstyle lettering, complex interlocking forms, dynamic motion, urban wall texture, {prompt}, spray-can energy",
        "negative_prompt": "clean font, photorealistic people, blur, watermark",
    },
    {
        "name": "Neon Cyber Delic",
        "prompt": "cyberpunk neon delic, saturated glows, reflective wet streets, stylized signage, {prompt}, futuristic noir atmosphere",
        "negative_prompt": "clear daylight photo, realistic faces, blur, watermark",
    },
    {
        "name": "Fractal Algorithmic",
        "prompt": "fractal algorithmic patterning, recursive geometry, mathematically generated ornament, {prompt}, infinite detail feel",
        "negative_prompt": "photo, lowres, blur, watermark",
    },
    {
        "name": "Generative Glitch",
        "prompt": "datamosh / generative glitch artifacts, color channel shifts, displaced geometry, {prompt}, digital decay aesthetic",
        "negative_prompt": "clean photo, perfect alignment, watermark",
    },
    {
        "name": "Solarized Poster",
        "prompt": "solarized high-contrast poster palette, inverted-like tones, bold silhouette, {prompt}, graphic punch",
        "negative_prompt": "photo, realistic skin tone, blur, watermark",
    },
    {
        "name": "Anachronistic Retro-Fab",
        "prompt": "anachronistic retro-fab collage, mixing eras and materials, whimsical juxtaposition, {prompt}, playful historical remix",
        "negative_prompt": "strict historical accuracy, modern realism, blur, watermark",
    },
    {
        "name": "Mechanical Blueprint Illustration",
        "prompt": "ornate mechanical illustration with engraved linework and brass textures implied, {prompt}, Victorian technical artistry",
        "negative_prompt": "photo, modern CAD realism, blur, watermark",
    },
    {
        "name": "Surrealist Automatism",
        "prompt": "automatic surrealist marks and juxtapositions, chance collage elements, dream associations, {prompt}, uncanny combinations",
        "negative_prompt": "photo, literal interpretations, blur, watermark",
    },
    {
        "name": "Biomorphic Organic",
        "prompt": "biomorphic organic forms, flesh-like textures blended with plant motifs, {prompt}, uncanny organic abstraction",
        "negative_prompt": "photo, straight realism, gore, watermark",
    },
    {
        "name": "Puppet / Marionette",
        "prompt": "puppet marionette aesthetic, jointed limbs, visible control rods, stage-like setting, {prompt}, theatrical handcrafted look",
        "negative_prompt": "real human faces, photorealistic skin, gore, blur, watermark",
    },
    {
        "name": "Silhouette Shadow Play",
        "prompt": "silhouette shadow-play composition, backlit forms, strong contrast, storytelling silhouettes, {prompt}, theatrical simplicity",
        "negative_prompt": "high detail texture, photorealistic, blur, watermark",
    },
    {
        "name": "Retro Toy Illustration",
        "prompt": "mid-century toy illustration, flattened perspective, cheerful colors, {prompt}, nostalgic children's merchandise art",
        "negative_prompt": "modern photorealism, gore, blur, watermark",
    },
    {
        "name": "Baroque Ornament",
        "prompt": "baroque ornamental flourish, rich curvilinear forms, sculptural drama, {prompt}, decorative opulence",
        "negative_prompt": "flat modernist, photorealistic portrait, blur, watermark",
    },
    {
        "name": "Expressionist Brushwork",
        "prompt": "expressionist painterly brushwork, emotive color clashes, gestural strokes, {prompt}, raw painterly energy",
        "negative_prompt": "photo, neat rendering, blur, watermark",
    },
    {
        "name": "Pulp Noir Illustration",
        "prompt": "pulp noir illustration, gritty shadows, rhythmic linework, cigarette smoke ambience, {prompt}, moody narrative tension",
        "negative_prompt": "bright cheerful, photorealistic, blur, watermark",
    },
    {
        "name": "Ink & Wash Portrait",
        "prompt": "ink line with tonal wash portrait, confident contour and diluted shading, {prompt}, artistic immediacy",
        "negative_prompt": "photo, heavy digital retouch, blur, watermark",
    },
    {
        "name": "Vintage Children's Illustration",
        "prompt": "vintage children's book illustration, soft halftones and quaint scenery, {prompt}, storybook nostalgia",
        "negative_prompt": "photorealistic, modern typography, blur, watermark",
    },
    {
        "name": "Retro Sci-Fi Comic",
        "prompt": "retro sci-fi comic art, bold panels, quirky machinery, {prompt}, pulp rocket-age enthusiasm",
        "negative_prompt": "realism, photographic detail, blur, watermark",
    },
    {
        "name": "Sticker Minimalist Mascot",
        "prompt": "minimal mascot sticker design, iconic silhouette, friendly pose, {prompt}, brandable charm",
        "negative_prompt": "photo, complex texture, blur, watermark",
    },
    {
        "name": "Hand-lettered Calligraphy",
        "prompt": "ornate hand-lettered calligraphy treatment, flourishes and ligatures, expressive pen strokes, {prompt}, typographic craftsmanship",
        "negative_prompt": "plain typed text, photorealistic scene, blur, watermark",
    },
    {
        "name": "Silhouette Cutout Animation",
        "prompt": "silhouette cutout animation style, layered shadow planes, simple moving shapes, {prompt}, folkloric vibe",
        "negative_prompt": "photo, color detail, blur, watermark",
    },
    {
        "name": "Embossed Relief",
        "prompt": "embossed relief look, raised edges and soft highlights, tactile letterpress impression, {prompt}, subtle depth",
        "negative_prompt": "flat glossy digital, blur, watermark",
    },
    {
        "name": "Moodboard Collage",
        "prompt": "editorial moodboard collage, varied textures and typographic snippets, {prompt}, concept exploration",
        "negative_prompt": "single photo, overly realistic, blur, watermark",
    },
    {
        "name": "Geode / Crystal Texture",
        "prompt": "geode crystal cross-section aesthetic, shimmering faceted forms, embedded minerals, {prompt}, ornamental geology",
        "negative_prompt": "plain flat color, blur, watermark",
    },
    {
        "name": "Stitched Felt Toy",
        "prompt": "stitched felt plush toy design, visible seams and felt nap, handmade charm, {prompt}, soft toy concept",
        "negative_prompt": "realistic human, gore, photorealistic skin, blur, watermark",
    },
    {
        "name": "Futuristic Iconography",
        "prompt": "futuristic icon set, simplified glyphs with subtle gradients and glow, {prompt}, UI/UX friendly",
        "negative_prompt": "photo, noisy texture, blur, watermark",
    },
    {
        "name": "Collaged Typography",
        "prompt": "typographic collage with torn letters, mixed typefaces, layered textures, {prompt}, rebellious editorial",
        "negative_prompt": "clean corporate logo, photorealistic, blur, watermark",
    },
    {
        "name": "Chiaroscuro Silhouette Painting",
        "prompt": "strong chiaroscuro silhouette painting, single light source drama, sculptural forms in shadow, {prompt}, theatrical intensity",
        "negative_prompt": "flat even lighting, pastel, photorealistic, watermark",
    },
    {
        "name": "Toy Stop-Motion Set",
        "prompt": "stop-motion toy set photography aesthetic, jointed figures, handcrafted props, visible armatures, {prompt}, tactile miniature world",
        "negative_prompt": "highly realistic human photo, gore, blur, watermark",
    },
    {
        "name": "Folk Art Naive",
        "prompt": "folk-art naive painting, flattened perspective, charming imperfections, {prompt}, hand-made cultural motifs",
        "negative_prompt": "photorealistic, modern shading, blur, watermark",
    },
    {
        "name": "Holographic Gradient",
        "prompt": "iridescent holographic gradient surfaces, shimmering pearlescent shifts, {prompt}, futuristic decorative sheen",
        "negative_prompt": "flat matte finish, photo, blur, watermark",
    },
    {
        "name": "Stencil Pattern Poster",
        "prompt": "bold stencil repeat poster, negative-space glyphs, strong composition, {prompt}, street-poster energy",
        "negative_prompt": "photorealistic, fine detail, blur, watermark",
    },
    {
        "name": "Silk Screen Urban Poster",
        "prompt": "silk-screen urban poster, limited palette, intentional printing imperfections, {prompt}, gritty graphic style",
        "negative_prompt": "high resolution photo, blur, watermark",
    },
    {
        "name": "Papercraft Origami Motif",
        "prompt": "origami-inspired folded paper motif, crisp crease lines, sculptural simplicity, {prompt}, geometric elegance",
        "negative_prompt": "photo, realistic skin texture, blur, watermark",
    },
    {
        "name": "Retro Catalog Illustration",
        "prompt": "mid-century catalog illustration, product-focused composition, simplified rendering, {prompt}, nostalgic advertising style",
        "negative_prompt": "modern photorealistic product shot, blur, watermark",
    },
    {
        "name": "Minimal Geometric Icon",
        "prompt": "minimal geometric icon design, reduced to essentials, clear silhouette, {prompt}, adaptable across sizes",
        "negative_prompt": "photo, texture, blur, watermark",
    },
    {
        "name": "Hand-stitched Needlepoint",
        "prompt": "needlepoint embroided texture simulation, grid-based stitching, {prompt}, cozy craft aesthetic",
        "negative_prompt": "photo, smooth vector, blur, watermark",
    },
    {
        "name": "Surreal Toybox",
        "prompt": "surreal toybox diorama, impossible connections between toys, whimsical absurdity, {prompt}, playful uncanny",
        "negative_prompt": "real gore, photorealistic adult themes, blur, watermark",
    },
    {
        "name": "M.C. Escher-style Tessellation",
        "prompt": "interlocking tessellation pattern that morphs between figures, impossible interplays, {prompt}, visual puzzle",
        "negative_prompt": "plain photo, blur, watermark",
    },
    {
        "name": "Cinematic Title Card",
        "prompt": "cinematic title card composition, dramatic typography and negative space, {prompt}, poster-grade mood",
        "negative_prompt": "photo, busy background, watermark, text artifacts",
    },
    {
        "name": "Tactile Felt Collage",
        "prompt": "felt and textile collage panels, visible fiber nap, soft overlaps, {prompt}, cozy handmade texture",
        "negative_prompt": "photo, glossy finish, blur, watermark",
    },
    {
        "name": "Retro Educational Diagram",
        "prompt": "vintage educational diagram styling, labeled cross-sections and friendly icons, {prompt}, analog schoolbook clarity",
        "negative_prompt": "modern UI, photorealistic, blur, watermark",
    },
    {
        "name": "Geometric Lowbrow",
        "prompt": "lowbrow pop-geometric hybrid, playful irreverence, simplified anatomy, {prompt}, bright contrasting shapes",
        "negative_prompt": "photorealistic, serious documentary tone, blur, watermark",
    },
    {
        "name": "Animated GIF-Like Loop",
        "prompt": "loopable GIF-friendly frame composition, clear repeated motion, flat colors, {prompt}, concise visual gag",
        "negative_prompt": "single static photo realism, blur, watermark",
    },
    {
        "name": "Faux-Vintage Halftone",
        "prompt": "faux-vintage halftone overlay, printed-on-paper feel, slightly misregistered color plates, {prompt}, retro printed charm",
        "negative_prompt": "clean digital photo, high gloss, watermark",
    },
    {
        "name": "Mosaic Pixel Collage",
        "prompt": "pixel mosaic collage, varied tile sizes and palettes, expressive low-res feel, {prompt}, handcrafted digital mosaic",
        "negative_prompt": "smooth gradients, photorealistic, blur, watermark",
    },
    {
        "name": "Puppet Shadow Theater",
        "prompt": "puppet shadow theater staging, layered silhouettes and lantern light, {prompt}, folk-story ambience",
        "negative_prompt": "photo realism, modern lighting, blur, watermark",
    },
    {
        "name": "Cutout Paper Puppet",
        "prompt": "paper puppet character design, articulated limbs and tabs, bold graphic colors, {prompt}, craft-friendly layout",
        "negative_prompt": "photorealism, gore, blur, watermark",
    },
    {
        "name": "Handcrafted Textile Print",
        "prompt": "screenprinted textile repeat, slight registration shifts, organic hand-printed feel, {prompt}, wearable pattern",
        "negative_prompt": "digital flat vector, photorealistic texture, blur, watermark",
    },
    {
        "name": "Kinetic Typography Diagram",
        "prompt": "kinetic typography frame, expressive letter motion implied in a single image, {prompt}, dynamic typographic layout",
        "negative_prompt": "static uninteresting text, photorealistic, blur, watermark",
    },
    {
        "name": "Typography 2",
        "prompt": "typography_art, english text, black background, photograph of a Fashion model {prompt}, highly detailed and intricate, golden ratio, vibrant colors, hyper maximalist, futuristic, city background, luxury, elite, cinematic, fashion, depth of field, colorful, glow, trending on artstation, ultra high definition",
        "negative_prompt": "Blurry, ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature, cut off, Low quality"
    }
]

styles = {k["name"]: (k["prompt"], k["negative_prompt"]) for k in style_list}