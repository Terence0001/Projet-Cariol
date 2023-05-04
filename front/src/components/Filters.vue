<script>
    import {request} from '../services/request.js'

    export default (await import('vue')).defineComponent({
        data(){
            return {
                colors: [
                    {color: 'Couleur', id: 0},
                    {color: 'rouge', id: 1},
                    {color: 'bleu', id: 2},

                ],
                selectedColor: 0
            }
        },
        
        methods: {
            loadFilters: function(){

            }
        }
    })
</script>

<template>
    <section id="filters-bar">
        <h3>Définiser les caractériques de votre voiture</h3>

        <div>
            <select v-model="selectedColor" >
                <option value="none" selected>Couleur</option>
                <option v-for="color in colors" :key="color" :value=color.id>{{ color.color }}</option>
            </select>
        </div>

    </section>
</template>