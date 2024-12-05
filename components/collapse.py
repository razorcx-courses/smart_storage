import streamlit.components.v1 as components

def collapse():
    # Use Streamlit's components.html to render custom HTML/JavaScript
    components.html(
        """
        <!-- Load required CDN scripts -->
        <!-- Tailwind CSS for styling -->
        <script src="https://cdn.tailwindcss.com"></script>
        <!-- Alpine.js collapse plugin for accordion functionality -->
        <script src="https://unpkg.com/@alpinejs/collapse@3.x.x/dist/cdn.min.js"></script>
        <!-- Alpine.js core library -->
        <script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
        
        <!-- Main accordion container with Alpine.js state management -->
        <!-- x-data initializes the accordion state, defaulting to panel1 being open -->
        <div x-data="{ activeAccordion: 'panel1' }" class="w-full max-w-md space-y-4">
            <!-- First accordion item -->
            <div class="border rounded-lg">
                <!-- Accordion header -->
                <div class="border-b">
                    <!-- Toggle button with click handler -->
                    <!-- If panel1 is active, clicking will close it (null), otherwise opens panel1 -->
                    <button 
                        @click="activeAccordion = activeAccordion === 'panel1' ? null : 'panel1'"
                        class="w-full px-4 py-3 text-left text-blue-600 hover:text-blue-800 focus:outline-none"
                    >
                        <span class="text-md font-medium">Collapsible Group Item #1</span>
                    </button>
                </div>
                <!-- Accordion content panel -->
                <!-- x-show controls visibility based on activeAccordion state -->
                <!-- x-collapse adds smooth animation when toggling -->
                <div 
                    x-show="activeAccordion === 'panel1'"
                    class="p-4 bg-white"
                >
                    Collapsible Group Item #1 content
                </div>
            </div>
            
            <!-- Second accordion item (same structure as first) -->
            <div class="border rounded-lg">
                <div class="border-b">
                    <button 
                        @click="activeAccordion = activeAccordion === 'panel2' ? null : 'panel2'"
                        class="w-full px-4 py-3 text-left text-blue-600 hover:text-blue-800 focus:outline-none"
                    >
                        <span class="text-md font-medium">Collapsible Group Item #2</span>
                    </button>
                </div>
                <div 
                    x-show="activeAccordion === 'panel2'"
                    class="p-4 bg-white"
                >
                    Collapsible Group Item #2 content
                </div>
            </div>
        </div>
        """,
        # Set fixed height for the component
        height=200
    )