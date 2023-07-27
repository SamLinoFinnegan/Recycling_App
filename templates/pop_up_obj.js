const htmlObject = {
    div: [
        {
        class: "popup",
        children: [
            {
            div: [
                {
                class: "bin_header_container",
                children: [
                    {
                    div: [
                        {
                        class: "warning_container",
                        children: [
                            {
                            div: [ 
                                {
                                class: "warning_wraper",
                                children: [
                                    {
                                    div: [{
                                        class: "warning_img_div",
                                        children: {
                                            img: {
                                                class: "warning_img",
                                                src: "../static/images/warning.png"
                                                }
                                            }
                                        }
                                    ]
                                    },
                                    {
                                    div: [
                                        {
                                        class: "warning_div",
                                        children: [
                                            {
                                            h4: {class: "dont_forget_msg",text: "Don't forget!"}
                                            },
                                            {
                                            h4: {class: "warning_message",text: "The trash must be thrown empty, without residues!"}
                                            }
                                        ]
                                        }
                                    ]
                                    }
                                ]
                                }
                            ]
                            }
                        ]
                        },
                        {
                        div: [
                            {
                            class: "dispose_msg_div",
                            children: [
                                {
                                h4: [{class: "dispose_msg", text: "Please deposit your item in the following bin"}]
                                }
                            ]
                            }
                        ]
                        }
                    ]
                    }
                ]
                },
                {
                div: [
                    {
                    class: "pop_up_img_div",
                    children: {img: {class: "pop_up_img",src: "../static/images/TakeAwayPaperBags.png"}
                        }
                    }
                ]
                },
                {
                div: [
                    {
                    class: "bin_container",
                    children: [
                        {
                        div: [
                            {
                            class: "name_bin_container",
                            children: [
                                {
                                h4: {class: "name", text: "Take Away Paper Bags"}
                                },
                                {
                                div:{
                                    class: "green",
                                    children: 
                                        {
                                        h4: {class: "undefined", text: "Dry Mixed Recycles"}
                                        }
                                    }
                                
                                }
                            ]
                            }
                        ]
                        }
                    ]
                    }
                ]
                }
            ]
            }
        ]
        }
    ]
    };